from rest_framework import serializers
from .models import Posts
from django.contrib.auth import get_user_model, authenticate

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Posts
		fields = ('id', 'title', 'description', 'authors')
		
class UserRegisterSirializer(serializers.ModelSerializer):
	class Mera:
		model = get_user_model()
		fields = '__all__'
		def create(self, clean_data):
			user_obj = UserModel.objects.create_user(email=clean_data['email'], password = clean_data['username'])
			user_obj.username =  clean_data['username']
			user_obj.save()
			return user_obj
		
class UserLoginSirializer(serializers.ModelSerializer):
	pass

class UserSirializer(serializers.ModelSerializer):
	pass