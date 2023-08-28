from django.contrib import admin
from .models import Posts, Profile

# Register your models here.
class apiPosts(admin.ModelAdmin):
	list_display =('title', 'description', 'authors')

admin.site.register(Posts, apiPosts)
admin.site.register(Profile)