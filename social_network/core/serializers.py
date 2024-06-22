from rest_framework import serializers
from .models import User, Discussion, Comment, Hashtag, Like, Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile_no', 'first_name', 'last_name']

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class DiscussionSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True)

    class Meta:
        model = Discussion
        fields = ['id', 'user', 'text', 'image', 'hashtags', 'created_on', 'view_count']

class CommentSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'discussion', 'text', 'created_on', 'likes']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'discussion', 'created_on']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'followed']
