from rest_framework import serializers
from reviews.models import User


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code', )


class SignUpSerializer(serializers.ModelSerializer):
    """Сериализатор для получение кода подтверждения."""
    class Meta:
        model = User
        fields = ('email', 'username')
