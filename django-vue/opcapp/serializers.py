from rest_framework import serializers
from .models import (RoleUser, Gender)


class RoleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleUser
        fields = ['id', 'name']


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'typeGender']