from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import PostSerializer
from .models import Posts

# Create your views here.
def main(request):
	return HttpResponse('sup bitchs')
	
class PostsView(generics.CreateAPIView):
	queryset = Posts.objects.all()
	serializer_class = PostSerializer
