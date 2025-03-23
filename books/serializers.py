from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book, AdminUser

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.get('email')

        # Check if the email already exists
        if AdminUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "An admin with this email already exists."})

        return AdminUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
