from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes= [IsOwnerOrReadOnly]
    filter_backends=[SearchFilter]
    search_fields=['title','content']

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

        

