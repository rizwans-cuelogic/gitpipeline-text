from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        read_only_fields  = ('id','password')

    def create(self, validated_data):
        user = User.objects.create(
                email = validated_data['email'],
                is_active = True
            )
        user.set_password(validated_data['password'])
        user.save()
        return user