# coding: utf-8

from django.utils import simplejson
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView

# fisl
from grade.models import Room, Area, Zone, Author, Talk

# twitter
from twitterauth.views import twitter_data


class TalkDetailView(DetailView):
    """ View utilizada para mostrar a palestra """

    model = Talk
    context_object_name = 'talk'


class TalkListView(TemplateView):
    """ View utilizada para mostrar as palestras """

    template_name = "grade/talks_list.html"

    def get_context_data(self, **kwargs):
        context = super(TalkListView, self).get_context_data(**kwargs)

        days = Talk.objects.dates("date", "day")
        hours = map(lambda x: str(x).zfill(2), range(9, 19))

        # twitter user data
        if hasattr(self.request.user, 'get_profile'):
            user_profile = self.request.user.get_profile()
            data = twitter_data(user_profile.oauth_token,
                                user_profile.oauth_secret)
            context['data'] = data

        context['days'] = days
        context['hours'] = hours

        return context


# def home(request):
#     talks = []
#     days = Talk.objects.dates("date", "day")
#     hours = Talk.objects.values_list("hour", flat=True).distinct()

#     for day in days:
#         for hour in hours:
#             talks.append(Talk.objects.filter(date=day, hour=hour))

#     return TemplateResponse(request, "grade/index.html",
#                             {'talks_by_day': talks})


def gerar_rooms(json):
    for room in json['rooms']:
        Room.objects.create(uid=room['room_id'],
                            capacity=room['capacity'],
                            name=room['name'],
                            translation=room['translation'],
                            position=room['position'])


def gerar_areas(json):
    for area in json['areas']:
        Area.objects.create(uid=area['area_id'], name=area['name'])


def gerar_zones(json):
    for zone in json['zones']:
        Zone.objects.create(uid=zone['zone_id'], name=zone['name'])


def gerar_authors(json):
    for author in json['authors']:
        Author.objects.create(uid=author['author_id'],
                              candidate=author['candidate'],
                              name=author['name'])


def gerar_talks(json):
    gerar_areas(json)
    gerar_rooms(json)
    gerar_zones(json)
    gerar_authors(json)

    for talk in json['talks']:
        t = Talk(area=Area.objects.get(uid=talk['area_id']),
                 room=Room.objects.get(uid=talk['room_id']),
                 zone=Zone.objects.get(uid=talk['zone_id']),
                 level=talk['level'],
                 hour=talk['hour'],
                 minute=talk['minute'],
                 date=talk['date'],
                 abstract=talk['abstract'],
                 title=talk['title'])

        # To get the id
        t.save()

        # Now we tie the authors to the talk
        t.authors = Author.objects.filter(candidate=talk['candidate'])
        t.save()


def gerar_grade(request):
    data_json = open("public/json/data.json", "r").read()
    json = simplejson.loads(data_json)

    gerar_talks(json)

    return HttpResponse("Grade gerada com sucesso!")
