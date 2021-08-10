from django.db import models
from django.contrib.auth.models import User


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(TimestampModel):
    name = models.CharField(max_length=255)
    registration_code = models.CharField(max_length=50, unique=True)
    established_on = models.DateField()
    address = models.TextField(null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class BoardMembers(TimestampModel):
    BOARD_MEMBERS = [
        ('Founder', 'Founder'),
        ('Co-Founder', 'Co-Founder'),
        ('Shareholder', 'Shareholder'),
        ('Director', 'Director'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, choices=BOARD_MEMBERS)
