from rest_framework import serializers

from .models import (Organization, BoardMembers)


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"


class BoardMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardMembers
        fields = "__all__"
