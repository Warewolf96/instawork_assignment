from django.conf.urls import url 
from django.contrib import admin

from .views import (
	TeamMemberListCreateAPIView,
	TeamMemberDetailAPIView,
	TeamMemberEditAPIView,
	TeamMemberDeleteAPIView,
	)


urlpatterns = [
    url('^$', TeamMemberListCreateAPIView.as_view(), name='list'),
    url('^(?P<pk>\d+)/$', TeamMemberDetailAPIView.as_view(), name='detail'),
    url('^(?P<pk>\d+)/edit/$', TeamMemberEditAPIView.as_view(), name='edit'),
    url('^(?P<pk>\d+)/delete/$', TeamMemberDeleteAPIView.as_view(), name='delete'),
]
