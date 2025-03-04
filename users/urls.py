from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('api/auth/register/', views.register_api, name='register'),
    path('api/auth/user/', views.get_user_data, name='user_data'),
    path('api/auth/login/', views.login_api, name='login'),
    path('api/auth/logout/', knox_views.LogoutView.as_view()),
    path('api/auth/logoutall/', knox_views.LogoutAllView.as_view()),
]