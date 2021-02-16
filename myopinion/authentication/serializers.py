from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=4, required=True, write_only=True)

    def validate(self, attrs: dict) -> dict:
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('Username must be alphanumeric')
        return attrs

    def create(self, validated_data: dict) -> User():
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
