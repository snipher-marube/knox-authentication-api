from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    # Use Knox's built-in LoginView for login
    path('login/', knox_views.LoginView.as_view(), name='knox_login'),

    # Custom views for registration and user data
    path('register/', views.register_api, name='register'),
    path('user/', views.get_user_data, name='user_data'),

    # Use Knox's built-in views for logout
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]