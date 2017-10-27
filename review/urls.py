from django.conf.urls import url

from review import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^new_company_review/$', views.new_company_review, name='new_company_review'),
    url(r'^company_review/$', views.company_review, name='company_review'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]