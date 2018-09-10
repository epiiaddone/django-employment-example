from django.conf.urls import url
from basic_app import views

#template tagging, django looks for app_name
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^other/$', views.other,name='other'),
    url(r'^index/$', views.index, name='index')

]
