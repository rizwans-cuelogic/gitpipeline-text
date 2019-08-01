from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from simplecrypt import encrypt, decrypt
from base64 import b64decode
from user_auth.models import User

class MyCustomAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            print("Meta",request.META.get('HTTP_AUTHORIZATION'))
            token = token.split(" ")[1]
            print("Token", token)
            token =  b64decode(token)
            print("Decoded Token", token)
            user_id = decrypt(settings.AUTH_SECRET, token)
            user = User.objects.get(id=user_id)
        except:
            raise exceptions.AuthenticationFailed('Invalid Authentication.')
        
        return(user,None)