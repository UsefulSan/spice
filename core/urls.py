from django.contrib.auth.views import LogoutView
from django.urls import path

from core import views

urlpatterns = [
    path('', views.UserViewSet.auth_page),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('main/', views.UserProfileView.as_view(), name='main'),
    path('main/', views.Graph.as_view(), name='graph'),
    # path('update_password/', views.UpdatePasswordView.as_view(), name='update_password'),
]
