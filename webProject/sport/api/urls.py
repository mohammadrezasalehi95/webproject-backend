from django.urls import path, re_path
from ..api import views

urlpatterns = [
    re_path(r'teamPage/gameResults/(?P<teamName>\w{0,50})',views.game_results,name="gameResults"),
    re_path(r'teamPage/teamMembers/(?P<teamName>\w{0,50})',views.team_members,name="teamMembers"),
    path('league/',views.LeaguesListView.as_view()),
    path('league/<int:pk>',views.LeagueDetailView.as_view()),
]