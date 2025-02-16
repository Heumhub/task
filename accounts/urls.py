from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
]
