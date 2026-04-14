from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    author= serializers.ReadOnlyField(source='author.username')
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields='__all__'