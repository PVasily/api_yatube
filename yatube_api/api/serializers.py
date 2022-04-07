from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post, Group, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False)

    class Meta:
        model = Comment
        fields = '__all__'
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
    posts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='group')

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')
