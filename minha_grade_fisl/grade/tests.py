from django.test import TestCase, Client
from django.utils import simplejson

from grade.views import gerar_rooms, gerar_areas, gerar_zones, gerar_authors, gerar_talks

from grade.models import Room, Area, Zone, Author, Talk

class TestViews(TestCase):
    def setUp(self):
        data_json = open("static_media/json/data.json", "r").read()
        self.json = simplejson.loads(data_json)

    def test_generate_room_from_json(self):
        gerar_rooms(self.json)
        self.assertEquals(len(Room.objects.all()), 12)

    def test_generate_areas_from_json(self):
        gerar_areas(self.json)
        self.assertEquals(len(Area.objects.all()), 22)

    def test_genereta_zone_from_json(self):
        gerar_zones(self.json)
        self.assertEquals(len(Zone.objects.all()), 7)

    def test_generate_author_from_json(self):
        gerar_authors(self.json)
        self.assertEquals(len(Author.objects.all()), 351)

    def test_generate_talk_from_json(self):
        gerar_talks(self.json)
        self.assertEquals(len(Talk.objects.all()), 300)

    def test_access_view_and_generate_talks(self):
        client = Client()
        response = client.get('/gerar_grade')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "Grade gerada com sucesso!")
