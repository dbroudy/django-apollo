from django.conf.urls import patterns, url

from landing import views

urlpatterns = patterns('',
    url(r'^register/(?P<button_id>\d+)/$', views.register),
    url(r'^questions/(?P<survey_id>\d+)$', views.questions),
    url(r'^(?P<slug>\w+)$', views.page),
)
