from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'teamPage/gameResults/(?P<teamName>\w{0,50})',game_results,name="gameResults"),
    re_path(r'teamPage/teamMembers/(?P<teamName>\w{0,50})',team_members,name="teamMembers"),
]

