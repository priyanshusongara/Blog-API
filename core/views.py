from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.shortcuts import render

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes=[AllowAny]

def home(request):
    return render(request,'home.html')