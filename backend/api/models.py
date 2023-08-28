from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	active = models.BooleanField(default=True)
	authors = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	
# Create your models here.
