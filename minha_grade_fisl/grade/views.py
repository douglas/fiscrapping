from django.utils import simplejson
from django.http import HttpResponse
from django.db import IntegrityError

from grade.models import Room, Area, Zone, Author, Talk

def gerar_rooms(json):
    for room in json['rooms']:
        Room.objects.create(uid=room['room_id'], capacity=room['capacity'], name=room['name'])

def gerar_areas(json):
    for area in json['areas']:
        Area.objects.create(uid=area['area_id'], name=area['name'])

def gerar_zones(json):
    for zone in json['zones']:
        Zone.objects.create(uid=zone['zone_id'], name=zone['name'])

def gerar_authors(json):
    for author in json['authors']:
        try:
            Author.objects.create(uid=author['candidate'], name=author['name'])
        except IntegrityError:
            pass

def gerar_talks(json):
    gerar_areas(json)
    gerar_rooms(json)
    gerar_zones(json)
    gerar_authors(json)

    for talk in json['talks']:
        try:
            Talk.objects.get_or_create(area=Area.objects.get(uid=talk['area_id']),
                                   room=Room.objects.get(uid=talk['room_id']),
                                   zone=Zone.objects.get(uid=talk['zone_id']),
                                   author=Author.objects.get(uid=talk['candidate']),
                                   level=talk['level'],
                                   hour=talk['hour'],
                                   minute=talk['minute'],
                                   date=talk['date'],
                                   abstract=talk['abstract'],
                                   title=talk['title'])
        except IntegrityError:
            pass

def gerar_grade(request):
    data_json = open("static_media/json/data.json", "r").read()
    json = simplejson.loads(data_json)

    gerar_talks(json)

    return HttpResponse("Grade gerada com sucesso!")
