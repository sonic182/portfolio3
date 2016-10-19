from django.conf.urls import url
# from django.conf import settings
# from django.contrib import admin
# from django.conf.urls.static import static

# from home import views as home_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='courses_index'),
    url(r'^(?P<id>[0-9]+)$', views.show, name='courses_show'),
    url(r'^thanks$', views.thanks, name='courses_thanks'),
]
