from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

from review import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^admin/', admin.site.urls),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^new_company_review/$', views.new_company_review, name='new_company_review'),
    url(r'^company_review/$', views.company_review, name='company_review'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    #url(r'^accounts/login/$', views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'review/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/review'}),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', CreateView.as_view(), name="api"),
    url(r'^api/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)