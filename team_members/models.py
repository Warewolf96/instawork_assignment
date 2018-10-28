from django.db import models


class TeamMember(models.Model):
    member_role = (
        (1, 'admin'),
        (0, 'regular'),
    )
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.IntegerField(choices=member_role, default=0)
