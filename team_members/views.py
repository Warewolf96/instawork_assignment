from django.shortcuts import render


from rest_framework.generics import(
	DestroyAPIView,
	ListCreateAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	)

from team_members.models import TeamMember 
from .serializers import TeamMemberListSerializer, TeamMemberDetailSerializer


class TeamMemberDetailAPIView(RetrieveAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamMemberDetailSerializer

class TeamMemberEditAPIView(UpdateAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamMemberDetailSerializer

	def put(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

class TeamMemberDeleteAPIView(DestroyAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamMemberDetailSerializer

class TeamMemberListCreateAPIView(ListCreateAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamMemberListSerializer
