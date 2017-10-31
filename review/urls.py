from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from review import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^new_company_review/$', views.new_company_review, name='new_company_review'),
    url(r'^company_review/$', views.company_review, name='company_review'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    #url(r'^accounts/login/$', views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'review/login.html'}, name='login'),
]