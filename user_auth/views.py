from django.shortcuts import render
# Create your views here.
from django.conf import settings
from rest_framework import generics,status
from .serializers import UserSerializer
from injazati import error_conf
from .system_error import check_for_registration_data
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from injazati.authentication import MyCustomAuthentication 

class UserCreateListView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request,*args,**kwargs):

        error = check_for_registration_data(request.data)

        if error:
            return Response(error,status=status.HTTP_412_PRECONDITION_FAILED)

        serializer = UserSerializer(data=request.data)



        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response({
                    "success":True,
                    "msg":"User Created Successfully.",
                    "user": serializer.data
                })
        print("Seializer Error", serializer.errors)
        return Response(
                error_conf.GENERICE_API_FAILURE,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserSigninView(APIView):

    def post(self,request,format=None):
        data = request.data
        print("Request", request.data)
        if not ( data.get('email') or data.get('password')):
            return Response(error_conf.LOGIN_ERROR,status.HTTP_400_BAD_REQUEST)

        email = data.get('email')
        password = data.get('password')
        user = User.objects.get(email=email)
        print("User",settings.AUTH_SECRET)
        if not user:
            return Response(error_conf.LOGIN_ERROR,
                            status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response(error_conf.LOGIN_ERROR,status.HTTP_400_BAD_REQUEST)

        token = encrypt(settings.AUTH_SECRET,str(user.id))
        token = b64encode(token)
        return Response({"success":True,
                    "msg":"token created successfully",
                    "token": token},status.HTTP_200_OK)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset= User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [MyCustomAuthentication]

    
    # permission_classes = [MyCustomAuthentication]