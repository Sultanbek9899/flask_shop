from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from src.apps.accounts.models import User
from src.apps.accounts.serializers import *

class UserGetViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    

class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    model = User
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user
    

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"message":"Wrond Old Password"}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({
                "message":"Password successfully updated!"
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]




class UserUpdateAPIView(generics.UpdateAPIView):
    model = User
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


    def get_object(self):
        return self.request.user