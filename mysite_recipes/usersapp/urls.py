from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]