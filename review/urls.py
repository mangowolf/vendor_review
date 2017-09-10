from django.conf.urls import url

from review import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^company_review/$', views.company_review, name='company_review'),
]