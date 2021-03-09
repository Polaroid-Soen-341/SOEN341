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
    #Serializer for creating a new user account

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'fullname', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 5},
                        'username': {'min_length': 3}}

    def create(self, validated_data):
        #Create a new user with encrypted password and return it
        return get_user_model().objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for viewing a user posts"""
    number_of_posts = serializers.SerializerMethodField()
    followed_by_req_user = serializers.SerializerMethodField()
    user_posts = serializers.SerializerMethodField('paginated_user_posts')

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'fullname',
                  'bio', 'profile_pic', 'number_of_followers',
                  'number_of_following', 'number_of_posts',
                  'user_posts', 'followed_by_req_user')

    def get_number_of_posts(self, obj):
        return Post.objects.filter(author=obj).count()

    def paginated_user_posts(self, obj):
        page_size = api_settings.PAGE_SIZE
        paginator = Paginator(obj.user_posts.all(), page_size)
        page = self.context['request'].query_params.get('page') or 1

        user_posts = paginator.page(page)
        serializer = UserPostsSerializer(user_posts, many=True)

        return serializer.data

    def get_followed_by_req_user(self, obj):
        user = self.context['request'].user
        return user in obj.followers.all()
