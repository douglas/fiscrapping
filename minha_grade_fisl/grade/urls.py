from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'grade.views.home', name='home'),
    url(r"^gerar_grade/", 'grade.views.gerar_grade', name="gerar_grade"),
)
