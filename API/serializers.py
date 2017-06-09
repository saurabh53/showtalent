from django.contrib.auth.models import User
from rest_framework import serializers
from API.models import Post


class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True,queryset=Post.objects.all())
	class Meta:
		model = User
		fields = ('id','username','password','posts')


class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Post
		fields = ('id','title','description','mediaFile','owner','category')


