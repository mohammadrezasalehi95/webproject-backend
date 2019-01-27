
from django.urls import path, re_path

from .views import *
from ..api import views

urlpatterns = [
    re_path(r'teamPage/gameResults/(?P<teamName>\w{0,50})',views.game_results,name="gameResults"),
    re_path(r'teamPage/teamMembers/(?P<teamName>\w{0,50})',views.team_members,name="teamMembers"),
    path('league/',views.LeaguesListView.as_view()),
    path('league/<int:pk>',views.LeagueDetailView.as_view()),
    re_path(r'playerPage/seasonDetail/(?P<pid>\d{0,50})', player_season_detail, name="seasonDetail"),
    re_path(r'playerPage/generalDetail/(?P<pid>\d{0,50})', player_general_detail, name="generalDetail"),
    re_path(r'gamePage/generalDetail/', game_general_detail),
    re_path(r'gamePage/specialDetail/', game_special_detail),
    re_path(r'gamePage/membersDetail/', game_members_detail),
    re_path(r'gamePage/eventLine/', game_eventLine),
    re_path(r'gamePage/gameReport/', game_report),

]
