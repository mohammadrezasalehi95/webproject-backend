from django.urls import path

from .views import ProfileViewSet

urlpatterns = [
    path('salam', ProfileViewSet.as_view, name='profile')
]