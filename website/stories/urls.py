from django.conf.urls import url
from . import views

app_name = 'stories'
urlpatterns = [
    # ex: /story/
    url(r'^$', views.index, name='index'),
    # ex: /story/5/
    url(r'^(?P<story_id>[0-9]+)', views.detail, name='story')
]