from  django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('register/',  views.UserRegisterView.as_view(), name='register'),
    path('auth-token/', auth_views.obtain_auth_token),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]