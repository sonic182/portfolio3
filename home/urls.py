from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name='homepage'),
    # url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^about$', views.about, name='about'),
    # url(r'^(?P<id>[0-9]+)$', views.show, name='courses_show'),
    # url(r'^thanks$', views.thanks, name='courses_thanks'),
]
