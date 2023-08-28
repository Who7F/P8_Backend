from django.urls import path
from .views import main, PostsView

urlpatterns = [
	path('', main),
	path('posts', PostsView.as_view())
]