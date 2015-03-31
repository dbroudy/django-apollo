from django.conf.urls import patterns, url

from landing import views

urlpatterns = patterns('',
    url(r'^register/(?P<button_id>\w+)/$', views.register),
    url(r'^questions$', views.questions),
    url(r'^(?P<slug>\w+)$', views.page),
)
