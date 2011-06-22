# Not needed here in this fisl talks parser for now, here in case of needing
# i.e, using scrapy native json serialization

from scrapy.item import Item, Field


class Talk(Item):
    title = Field()
    abstract = Field()
    area_id = Field()
    author_id = Field()
    date = Field()
    hour = Field()
    minute = Field()
    room_id = Field()
    level = Field()
    zone_id = Field()


class Room(Item):
    uid = Field()
    name = Field()
    capacity = Field()


class Zone(Item):
    uid = Field()
    name = Field()


class Author(Item):
    uid = Field()
    name = Field()


class Area(Item):
    uid = Field()
    name = Field()
    description = Field()
