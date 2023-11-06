from django.urls import path, include
from users.views import Register
from .views import CustomLoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('users/login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/registration/password_reset_form.html'), name='password_reset'),


]
