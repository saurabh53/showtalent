from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class TokenAuth(authentication.TokenAuthentication):
	def authenticate(self,request):
		token = request.META.get('HTTP_AUTHENTICATION')
		username = request.META.get('X_USERNAME')
		if not token or not username:
			return False
		try:
			user = User.objects.get(username=username)
			
		except User.DoesNotExist:
			raise exceptions.AuthenticationFailed('No such user')
		return True
			
			