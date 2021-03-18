#from django.contrib.auth.models import get_user_model
from rest_framework.settings import api_settings
from rest_framework import serializers
from django.contrib.auth import get_user_model  


#original 

#class UserSerializer(serializers.ModelSerializer):
 #   class Meta:
 #       model = PolaroidUser
  #      fields = ('username', 'password', 'email', 'first_name', 'last_name')
   #     extra_kwargs = {'password': {'write_only': True}}
#
 #   def create(self, validated_data):
  #      password = validated_data.pop('password')
   #    user.set_password(password)
    #    user.save()
     #   return user

        #add email must need to add email 


#from the example code 

class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for creating a new user account"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username','firstName', 'lastName', 'birthday', 'password')

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
