from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)