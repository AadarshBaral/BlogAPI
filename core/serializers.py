from rest_framework import serializers
from . models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]
    def create(self,validated_data):
        user = User.objects.create(username= validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ["title","author","publish","updated","status","content"]
        
