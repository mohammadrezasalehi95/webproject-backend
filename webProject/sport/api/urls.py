from django.urls import path

from .views import ProfileViewSet, GameResults

urlpatterns = [
    path('salam', ProfileViewSet.as_view, name='profile'),
    path(r'GameResults/(?P<teamName>\w{0,50})',GameResults.as_view()),
]