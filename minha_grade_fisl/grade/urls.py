from django.conf.urls.defaults import patterns, url
from views import TalkListView, TalkDetailView

urlpatterns = patterns('grade.views',
    url(r'^$', TalkListView.as_view(), name='talks'),
    url(r'^palestras/(?P<pk>\d+)/$', TalkDetailView.as_view(),
        name='talk'),

    url(r"^gerar_grade/", 'gerar_grade', name="gerar_grade"),
)
