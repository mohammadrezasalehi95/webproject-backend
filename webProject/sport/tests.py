from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory

from sport.api.views import *


class getTestCase(TestCase):
    def test_login_user(self):

        factory = APIRequestFactory()
        SiteUser.objects.create(username='olivia')
        user = SiteUser.objects.get(username='olivia')
        view = is_login

        request = factory.get('/isLogin/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response, True)

    def test_favorite_game(self):

        factory = APIRequestFactory()
        SiteUser.objects.create(username='olivia')
        game = Game.objects.get(team1="barsa",team2="real",date="2019-01-27")
        user = SiteUser.objects.get(username='olivia')
        user.favoriteGames.add(game)
        view = favorite_games

        request = factory.get('/mainPage/favoriteNews')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data[0],game)


    def test_favorite_new(self):

        factory = APIRequestFactory()
        SiteUser.objects.create(username='olivia')
        new = New.objects.get(id=1)
        user = SiteUser.objects.get(username='olivia')
        user.favoriteNews.add(new)
        view = favorite_news

        request = factory.get('/mainPage/favoriteGames')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data[0], new)

    def test_new_like_number(self):

        factory = APIRequestFactory()
        SiteUser.objects.create(username='olivia')
        new = New.objects.get(id=1)
        user = SiteUser.objects.get(username='olivia')
        view = add_favorite_new

        request = factory.get('/newPage/addFavorite')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.data[0].likes, 1)

