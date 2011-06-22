from django.utils import simplejson
from django.http import HttpResponse

from grade.models import Room, Area, Zone, Author, Talk

def gerar_rooms(json):
    for room in json['rooms']:
        Room.objects.create(uid=room['uid'], capacity=room['capacity'], name=room['name'])

def gerar_areas(json):
    for area in json['areas']:
        Area.objects.create(uid=area['uid'], name=area['name'])

def gerar_zones(json):
    for zone in json['zones']:
        Zone.objects.create(uid=zone['uid'], name=zone['name'])

def gerar_authors(json):
    for author in json['authors']:
        Author.objects.get_or_create(uid=author['uid'], name=author['name'])

def gerar_talks(json):
    gerar_areas(json)
    gerar_rooms(json)
    gerar_zones(json)
    gerar_authors(json)

    for talk in json['talks']:
        Talk.objects.get_or_create(area=Area.objects.get(uid=talk['area_id']),
                                   room=Room.objects.get(uid=talk['room_id']),
                                   zone=Zone.objects.get(uid=talk['zone_id']),
                                   author=Author.objects.get(uid=talk['author_id']),
                                   level=talk['level'],
                                   hour=talk['hour'],
                                   minute=talk['minute'],
                                   date=talk['date'],
                                   abstract=talk['abstract'],
                                   title=talk['title'])

def gerar_grade(request):
    data_json = open("static_media/json/data.json", "r").read()
    json = simplejson.loads(data_json)

    gerar_talks(json)

    return HttpResponse("Grade gerada com sucesso!")
