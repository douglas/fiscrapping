from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.utils import simplejson

from grade.views import gerar_rooms, gerar_areas, gerar_zones, gerar_authors
from grade.views import gerar_talks
from grade.views import clean_data

from grade.models import Room, Area, Zone, Author, Talk


class TestViews(TestCase):
    def setUp(self):
        data_json = open("public/json/data.json", "r").read()
        self.json = simplejson.loads(data_json)

        self.factory = RequestFactory()

    def test_roomset_is_empty(self):
        clean_data()

        self.assertEquals(Room.objects.count(), 0)

    def test_areaset_is_empty(self):
        clean_data()

        self.assertEquals(Area.objects.count(), 0)

    def test_zoneset_is_empty(self):
        clean_data()

        self.assertEquals(Zone.objects.count(), 0)

    def test_authorset_is_empty(self):
        clean_data()

        self.assertEquals(Author.objects.count(), 0)

    def test_talkset_is_empty(self):
        clean_data()

        self.assertEquals(Talk.objects.count(), 0)

    def test_generate_room_from_json(self):
        gerar_rooms(self.json)
        self.assertEquals(Room.objects.count(), 12)

    def test_generate_areas_from_json(self):
        gerar_areas(self.json)
        self.assertEquals(Area.objects.count(), 22)

    def test_genereta_zone_from_json(self):
        gerar_zones(self.json)
        self.assertEquals(Zone.objects.count(), 7)

    def test_generate_author_from_json(self):
        gerar_authors(self.json)
        self.assertEquals(Author.objects.count(), 511)

    def test_generate_talk_from_json(self):
        gerar_talks(self.json)
        self.assertEquals(Talk.objects.count(), 362)

    def test_access_view_and_generate_talks(self):
        client = Client()
        response = client.get('/gerar_grade/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, "Grade gerada com sucesso!")

    def test_access_home_and_see_all_talks(self):
        # TODO: Use splinter to test browser access

        client = Client()
        response = client.get('/')

        self.assertEquals(response.status_code, 200)
