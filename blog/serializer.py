from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from users.models import Profile

class JsonPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class JsonProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class JsonUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'