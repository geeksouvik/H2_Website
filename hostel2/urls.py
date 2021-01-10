from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.base, name = 'blog'),
    path('home/', views.home, name = "home_page"),
    path('gallery/', views.gallery, name="gallery"),
    path('contactus/', views.contactus , name="contactus"),
    path('legend/', views.legend , name="legend"),
    path('alumni/', views.alumni , name="alumni"),

    path('activities/', PostListView.as_view() , name="blog-home"),
    path('activities/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('activities/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('activities/post/new/', PostCreateView.as_view(), name='post-create'),
    path('activities/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('activities/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


]

