"""
URL configuration for rideproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from rideapp.views import UserViewSet, LoginViewSet,CreateRideView, RideDetailView, ListRidesView,UpdateRideStatusView
router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('rideapi/ridedetails/create/', CreateRideView.as_view(), name='ride-create'),
    path('rideapi/ridedetails/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('rideapi/ridedetails/', ListRidesView.as_view(), name='ride-list'),
    path('rideapi/ridedetails/<int:pk>/update-status/', UpdateRideStatusView.as_view(), name='ride-update-status'),
]
