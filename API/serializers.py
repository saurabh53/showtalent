from django.contrib.auth.models import User
from rest_framework import serializers
from API.models import Post
from API.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True,queryset=Post.objects.all())
	profile = serializers.PrimaryKeyRelatedField(many=True,queryset=UserProfile.objects.all())
	class Meta:
		model = User
		fields = ('id','username','password','first_name','last_name','email','posts','profile')
		write_only_field = ('password',)
	def create(self,validated_data):
		user = User(
			email = validated_data['email'],
			username = validated_data['username'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user


class PostSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Post
		fields = ('id','title','description','mediaFile','owner','category')


class ProfileSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = UserProfile
		fields = ('id','created','owner','city','photo','phone','country','bio','website')
