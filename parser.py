from xml.etree import ElementTree

import os
import contextlib
import urllib
import json

url = "http://fisl.org.br/12/papers_ng/public/fast_grid?event_id=1"

# We are using a context manager here so we dont need to worry about
# closing the stream
with contextlib.closing(urllib.urlopen(url)) as f:
    tree = ElementTree.parse(f)

# Find the elements using xpath expressions
talks = tree.findall('.//slot')
zones = tree.findall('.//zones/zone')
authors = tree.findall('.//authorship/person')
areas = tree.findall('.//areas/area')
rooms = tree.findall('.//rooms/room')

info = {'talks': [],
        'zones': [],
        'authors': [],
        'areas': [],
        'rooms': []}

for talk in talks:
    data = {'title': talk.attrib.get("title"),
            'abstract': talk.attrib.get("abstract"),
            'area_id': talk.attrib.get("area"),
            'candidate': talk.attrib.get("candidate"),
            'date': talk.attrib.get("date"),
            'hour': talk.attrib.get("hour"),
            'minute': talk.attrib.get("minute"),
            'room_id': talk.attrib.get("room"),
            'level': talk.attrib.get("level"),
            'zone_id': talk.attrib.get("zone")}

    info['talks'].append(data)

for zone in zones:
    data = {'zone_id': zone.attrib['id'],
            'name': zone.find("name").text}

    info['zones'].append(data)

for author in authors:
    data = {'author_id': author.attrib.get("id"),
            'name': author.attrib.get("name"),
            'candidate': author.attrib.get("candidate")}

    info['authors'].append(data)

for room in rooms:
    data = {'room_id': room.attrib.get("id"),
            'name': room.find("name").text,
            'capacity': room.find("capacity").text,
            'translation': room.find("translation").text,
            'position': room.find("position").text}

    info['rooms'].append(data)

for area in areas:
    data = {'area_id': area.attrib.get("id"),
            'name': area.find("name").text,
            'description': area.find("descr").text}

    info['areas'].append(data)

# now we store the data in json, so we can unserialize later
# and send it to a database. Perhaps it would be better to split files
# so we can do selective load, but for now (small set of data) it is
# ok to keep as it is.
filename = os.path.join("output", "data.json")
with open(filename, "w") as f:
    f.write(json.dumps(info))

# Lets save the for inspection if needed
filename = os.path.join("output", "data.xml")
tree.write(filename, encoding="utf-8")
