from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "profile_picture")

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "email", "password", "bio", "profile_picture")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email", ""),
            password=validated_data.get("password"),
        )
        user.bio = validated_data.get("bio", "")
        user.profile_picture = validated_data.get("profile_picture", None)
        user.save()

        # token retrieval/creation
        Token.objects.create(user=user)
        return user
