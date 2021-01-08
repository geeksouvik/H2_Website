
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hostel2.urls')),
    path('register/', user_views.registerPage, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
    path('profile_update/', user_views.profile_update, name = 'profile_update'),
    path('login/', user_views.loginPage, name = 'login'),
    path('logout/', user_views.logoutPage, name = 'logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
