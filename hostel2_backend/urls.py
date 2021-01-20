
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import VerificationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hostel2.urls')),
    path('register/', user_views.registerPage, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
    path('profile_update/', user_views.profile_update, name = 'profile_update'),
    path('login/', user_views.loginPage, name = 'login'),
    path('logout/', user_views.logoutPage, name = 'logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name = 'password_reset'),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = "hostel2.views.error_404_view"