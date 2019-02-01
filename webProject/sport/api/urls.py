from allauth.account.views import ConfirmEmailView, confirm_email
from django.urls import path, re_path, include

from .views import *
from ..api import views

urlpatterns = [
    path('', test),
    re_path(r'teamPage/gameResults/(?P<teamName>\w{0,50})', views.game_results, name="gameResults"),
    re_path(r'teamPage/teamMembers/(?P<teamName>\w{0,50})', views.team_members, name="teamMembers"),
    re_path(r'teamPage/teamNews/(?P<teamName>\w{0,50})', views.team_news),
    path('accounts/', include('allauth.urls')),
    path('competition/', views.CompetitionListView.as_view()),
    path('competition/game/<str:competition_name>', views.CompetitionGameView.as_view()),
    path('competition/league/<str:league_name>', views.LeagueRowView.as_view()),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path('^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email,
            name='account_confirm_email'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/users', views.UserListView.as_view()),
    re_path(r'playerPage/seasonDetail/(?P<pid>\d{0,50})', player_season_detail, name="seasonDetail"),
    re_path(r'playerPage/generalDetail/(?P<pid>\d{0,50})', player_general_detail, name="generalDetail"),
    re_path(r'playerPage/playerNews/(?P<pid>\d{0,50})', player_news),
    re_path(r'gamePage/generalDetail/', game_general_detail),
    re_path(r'gamePage/specialDetail/', game_special_detail),
    re_path(r'gamePage/membersDetail/', game_members_detail),
    re_path(r'gamePage/eventLine/', game_eventLine),
    re_path(r'gamePage/gameReport/', game_report),
    re_path(r'gamePage/gameNews/', game_news),
    re_path(r'gamePage/addFavorite/', add_favorite_game),
    re_path(r'mainPage/lastNews', last_news),
    re_path(r'mainPage/favoriteNews', favorite_news),
    re_path(r'mainPage/allGames', games),
    re_path(r'mainPage/favoriteGames', favorite_games),
    re_path(r'newPage/data/(?P<pk>\d{0,50})', new_data),
    re_path(r'newPage/comments/(?P<pk>\d{0,50})', new_comments),
    re_path(r'newPage/addComment/(?P<pk>\d{0,50})', add_comment),
    re_path(r'newPage/related/(?P<pk>\d{0,50})', related_news),
    re_path(r'newPage/addFavorite/(?P<pk>\d{0,50})', add_favorite_new),
    re_path(r'isLogin', is_login),
]


def a(request, *args):
    print('salam')
