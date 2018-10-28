from rest_framework.serializers import ModelSerializer

from team_members.models import TeamMember


class TeamMemberListSerializer(ModelSerializer):
	class Meta:
		model = TeamMember
		fields = '__all__'



class TeamMemberDetailSerializer(ModelSerializer):
	class Meta:
		model = TeamMember
		fields = '__all__'
