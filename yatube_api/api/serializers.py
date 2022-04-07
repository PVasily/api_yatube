from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Group, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field='slug',
        required=False)
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'group',
            'author',
            'image',
            'pub_date',
            'comments')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        many=True,
        read_only=True)

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')
