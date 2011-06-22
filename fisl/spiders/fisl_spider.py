from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector

import os

try:
    import json
except ImportError:
    import simplejson as json


def get_text(obj, xpath):
    """
    Dont mind this code, it will serve as a base for a little patch to scrapy's
    XPathSelector so it could work as django's values_list with the flat=True
    argument.
    """

    data = obj.select(xpath)

    if not data:
        return ""
    elif len(data) == 1:
        return data[0].extract()
    else:
        raise AssertionError('You xpath expr should return one or zero items')


class TalksSpider(BaseSpider):
    name = "fisl.org.br"
    allowed_domains = ["fisl.org.br"]
    start_urls = [
        "http://fisl.org.br/12/papers_ng/public/fast_grid?event_id=1",
    ]

    def parse(self, response, save_data=True):
        """ Parse fisl data """

        # working set of data, so it helps to define what to scrap
        if save_data:
            filename = os.path.join("output", "data.xml")
            open(filename, 'wb').write(response.body)

        xxs = XmlXPathSelector(response)

        talks = xxs.select('//slot')
        zones = xxs.select('//zones/zone')
        authors = xxs.select('//authorship/person')
        areas = xxs.select('//areas/area')
        rooms = xxs.select('//rooms/room')

        info = {'talks': [],
                'zones': [],
                'authors': [],
                'areas': [],
                'rooms': []}

        for talk in talks:
            data = {'title': get_text(talk, "@title"),
                    'abstract': get_text(talk, "@abstract"),
                    'area_id': get_text(talk, "@area"),
                    'candidate': get_text(talk, "@candidate"),
                    'date': get_text(talk, "@date"),
                    'hour': get_text(talk, "@hour"),
                    'minute': get_text(talk, "@minute"),
                    'room_id': get_text(talk, "@room"),
                    'level': get_text(talk, "@level"),
                    'zone_id': get_text(talk, "@zone")}

            info['talks'].append(data)

        for zone in zones:
            data = {'zone_id': get_text(zone, "@id"),
                    'name': get_text(zone, "name/text()")}

            info['zones'].append(data)

        for author in authors:
            data = {'author_id': get_text(author, "@id"),
                    'name': get_text(author, "@name"),
                    'candidate': get_text(author, "@candidate")}

            info['authors'].append(data)

        for room in rooms:
            data = {'room_id': get_text(room, "@id"),
                    'name': get_text(room, "name/text()"),
                    'capacity': get_text(room, "capacity/text()"),
                    'translation': get_text(room, "translation/text()"),
                    'position': get_text(room, "position/text()")}

            info['rooms'].append(data)

        for area in areas:
            data = {'area_id': get_text(area, "@id"),
                    'name': get_text(area, "name/text()"),
                    'description': get_text(area, "descr/text()")}

            info['areas'].append(data)

        # now we store the data in json, so we can unserialize later
        # and send it to a database. Perhaps it would be better to split files
        # so we can do selective load, but for now (small set of data) it is
        # ok to keep as it is.
        filename = os.path.join("output", "data.json")
        open(filename, "w").write(json.dumps(info))
