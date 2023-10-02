from django.urls import path
from .views import main, PostsView

urlpatterns = [
	path('', main),
	path('posts', PostsView.as_view()),
	##path('register'),
	##path('login'),
	##path('logout'),
	##path('user'),
]