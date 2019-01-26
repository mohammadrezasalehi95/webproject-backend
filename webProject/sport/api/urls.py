from django.urls import path, re_path
from rest_framework import routers
# router=routers.DefaultRouter()
# router.register(r'gameResults/(?P<teamName>\w{0,50})',GameResults.as_view())
from sport.api.views import *

urlpatterns = [
    # path('salam', ProfileViewSet.as_view(), name='profile'),
    re_path(r'teamPage/gameResults/(?P<teamName>\w{0,50})',game_results,name="gameResults"),
    re_path(r'teamPage/teamMembers/(?P<teamName>\w{0,50})',team_members,name="teamMembers"),
]
