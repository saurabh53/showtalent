# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from rest_framework import permissions
from django.contrib.auth.models import User
from API.serializers import UserSerializer,PostSerializer,ProfileSerializer
from rest_framework import generics
from API.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from API.auth import TokenAuth
from API.models import Post
from API.models import UserProfile
from django.conf import settings


class PostListOnCategory(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = PostSerializer
	def get_queryset(self):
		category = self.request.GET.get('category')
		if category == None:
			return JsonResponse({'detail':'Please provide category'},status=400)
		queryset = Post.objects.filter(owner=self.request.user).filter(category=category)
		return queryset



class PostList(generics.ListCreateAPIView):

    #queryset = Post.objects.filter(owner=request.user)
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
		# print settings.TRIE.start_with_prefix('jumbo')
		queryset = Post.objects.filter(owner=self.request.user)
		return queryset
    def perform_create(self,serializer):
		category = self.request.POST.get('category')
		if category ==None:
			category = ''
		print 'category',category
		if not settings.TRIE.has_word(category):
			print 'Cat ',category
			settings.TRIE.add(category)
		serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
    	queryset = Post.objects.filter(owner=self.request.user)
    	return queryset

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #queryset = Post.objects.all()
    serializer_class = ProfileSerializer
    def perform_update(self,serializer):
    	instance = serializer.save()
    	#print 'Updated '+instance.owner
    def get_object(self):
    	queryset = self.get_queryset()
    	return queryset[0]

    def get_queryset(self):
    	print self.request.user
    	queryset = UserProfile.objects.filter(owner=self.request.user)
    	print 'queryset ',queryset[0].owner
    	return queryset


class UserRegistration(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.AllowAny,)
	def perform_create(self,serializer):
		return serializer.save()


class UserList(generics.RetrieveUpdateDestroyAPIView):
	#authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)
	queryset=User.objects.all()
	serializer_class = UserSerializer
	
@csrf_exempt
def logout_user(request):
	return JsonResponse({'request':request.session['auth']},safe=False,status=200) 

@csrf_exempt
def get_auth_token(request):
	print '-----request-------'
	print request.POST
	print '------end-----------'
	username = request.POST.get('username')
	password = request.POST.get('password')
	print username,password
	user = authenticate(username=username,password=password)
	print 'user --- ',user
	if user is not None:
		if user.is_active:
			token,created = Token.objects.get_or_create(user=user)
			request.session['auth'] = token.key
			print '----token----',token.key
			return JsonResponse({'token':token.key},safe=False,status=200)
			#return redirect(settings.LOGIN_URL,request)
			#return render(request,'<h1>done right..</h1>',{})
	return redirect(settings.LOGIN_URL,request)	

@csrf_exempt
def get_query(request):
	qP = request.GET.get('qP')
	print 'qP',qP
	if not qP == None:
		q = settings.TRIE.start_with_prefix(qP)
		return JsonResponse({'qP':q})
	return JsonResponse({'detail':'Please provide query parameter'})	

