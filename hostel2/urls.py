from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name = 'landing_page'),
    path('home/', views.home, name = "home_page"),
    path('gallery/', views.gallery, name="gallery"),
    path('contactus/', views.contactus , name="contactus"),
    path('legend/', views.legend , name="legend"),
    path('alumni/', views.alumni , name="alumni"),

]

