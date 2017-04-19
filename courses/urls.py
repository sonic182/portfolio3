from courses import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='courses_index'),
    url(r'^(?P<_id>[0-9]+)$', views.show, name='courses_show'),
    url(r'^(?P<_id>[0-9]+)/preview$', views.preview, name='courses_preview'),
    url(r'^thanks$', views.thanks, name='courses_thanks'),
]
