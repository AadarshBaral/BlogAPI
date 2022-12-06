from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from . models import Post
from . serializers import PostSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User

class PostCreateList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        try:
            
            return Post.objects.all().filter(author = self.request.user,status=Post.Status.PUBLISHED )
        except:
            return Post.objects.filter(status=Post.Status.PUBLISHED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        try:
            return Post.objects.all().filter(author = self.request.user,status=Post.Status.PUBLISHED )
        except:
            return Post.objects.filter(status=Post.Status.PUBLISHED)
    
class UserReg(APIView):
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user= user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj)})
        

post_view_create = PostCreateList.as_view()
post_edit  = PostRetriveUpdateDelete.as_view()
register  = UserReg.as_view()