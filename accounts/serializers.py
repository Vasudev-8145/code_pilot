
from rest_framework import serializers

from accounts.models import User,StudentProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

class ProfileSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField()

    class Meta:

        model = StudentProfile

        fields = "__all__"

        read_only_fields = ["id","student"]

