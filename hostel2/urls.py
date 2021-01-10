from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.base, name = 'blog'),
    path('home/', views.home, name = "home_page"),
    path('gallery/', views.gallery, name="gallery"),
    path('contactus/', views.contactus , name="contactus"),
    path('legend/', views.legend , name="legend"),
    path('alumni/', views.alumni , name="alumni"),
<<<<<<< HEAD
    path('activities/', PostListView.as_view() , name="blog-home"),
    path('activities/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('activities/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('activities/post/new/', PostCreateView.as_view(), name='post-create'),
    path('activities/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('activities/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
=======
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('blog/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

>>>>>>> b5655ff9393267571f48b30e887ca2fb74792088

]

