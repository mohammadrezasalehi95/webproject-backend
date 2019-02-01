import operator
from functools import reduce

from django.db.models import Q, F
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions
from rest_framework.response import Response
from datetime import datetime, timedelta

from .serializers import *
from rest_framework import generics


class UserListView(generics.ListCreateAPIView):
    queryset = SiteUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def game_results(request, teamName):
    sortBy = request.query_params.get('sort')

    if request.method == 'GET':
        query = Game.objects.filter(Q(team1__name=teamName))
        if sortBy == "win":
            query = query.order_by().order_by('-status')[:10]
        elif sortBy == "loose":
            query = query.order_by().order_by('status')[:10]
        elif sortBy == "side":
            query = query.order_by().order_by('-team2_name')[:10]
        elif sortBy == "date":
            query = query.order_by().order_by('-date')[:10]

        serializer = GameResultSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def team_members(request, teamName):
    if request.method == 'GET':
        query = Team.objects.get(name=teamName)
        members = query.profile_set
        serializer = MemberTeamSerializer(members, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def team_news(request, teamName):
    if request.method == 'GET':
        query = New.objects.filter(title__contains=teamName).order_by('-releaseTime')[:30]
        serializer = NewSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def player_news(request, pid):
    if request.method == 'GET':
        player = Profile.objects.get(pid=pid)
        query = New.objects.filter(title__contains=player.name).order_by('-releaseTime')[:30]
        serializer = NewSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_data(request, pk):
    if request.method == 'GET':
        new = New.objects.get(pk=pk)
        serializer = NewSerializer(new)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def related_news(request, pk):
    if request.method == 'GET':
        new = New.objects.get(pk=pk)
        if new.relateds.count():
            serializer = NewSerializer(new.relateds, many=True)

        else:
            query = New.objects.filter(reduce(operator.or_, (Q(title__icontains=x) for x in new.subtitle.split('_'))))
            serializer = NewSerializer(query, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def new_comments(request, pk):
    if request.method == 'GET':
        new = New.objects.get(pk=pk)
        query = new.comment_set
        serializer = CommentSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def add_comment(request, pk):
    if request.method == 'POST':
        new = New.objects.get(pk=pk)
        new.comment_set.create(text=request.data['text'])

        return Response({})


@api_view(['GET', 'POST'])
def add_favorite_new(request, pk):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            print("**********")
        new = New.objects.get(pk=pk)
        new.likes += 1
        new.save()
        # request.user.favoriteNews.add(new)
        return Response({})


@api_view(['GET', 'POST'])
def add_favorite_game(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    user = request.user

    if request.method == 'POST':
        if user.is_authenticated:
            print("**********")

        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]
        game.likes += 1
        game.save()
        # request.user.favoriteGames.add(game)

        return Response({})


@api_view(['GET', 'POST'])
def is_login(request):
    key = request.query_params.get('key')
    print()
    if request.method == 'GET':
        print(request.user)
        return Response(request.user.is_authenticated)


@api_view(['GET', 'POST'])
def game_news(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]

        news = game.news
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def player_season_detail(request, pid):
    print(type(pid))
    if request.method == 'GET':
        player = Profile.objects.get(pid=pid)
        print(player.type)

        if player.type == "F":
            details = player.footballseasondetail_set
            serializer = FootBallSeasonDetailSerializer(details, many=True)

        elif player.type == "B":
            details = player.basketseasondetail_set
            serializer = BasketSeasonDetailSerializer(details, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def player_general_detail(request, pid):
    if request.method == 'GET':
        player = Profile.objects.filter(pid=pid)
        serializer = ProfileSerializer(player, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def game_general_detail(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)
        serializer = GameResultSerializer(game, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def game_special_detail(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]

        gameSpecialDetail = game.gamespecialdetail_set
        serializer = GameSpecialDetailSerializer(gameSpecialDetail, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def game_report(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]
        gameReport = Game_Report.objects.get(game=game)
        serializer = GameReportSerializer(gameReport)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def game_members_detail(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]
        gamePlayersDetail = game.game_player_set
        serializer = GameMembersDetailSerializer(gamePlayersDetail, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def last_news(request):
    limit = request.query_params.get('limit')
    limit = int(limit)
    if request.method == 'GET':
        query = New.objects.all().order_by('-releaseTime')[:limit]
        serializer = NewSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def favorite_news(request):
    # user = request.query_params.get('user')
    if request.method == 'GET':
        user = request.user
        # if user.is_authenticated:
            # query = User.objects.get(user=user)
        down_side = datetime.now() - timedelta(days=1)
        up_side = datetime.now() + timedelta(days=1)
        favoriteNews = New.objects.filter(releaseTime__gt=down_side, siteuser=user, releaseTime__lt=up_side)
        serializer = NewSerializer(favoriteNews, many=True)
        return Response(serializer.data)
    # else:
    #     return Response({})


@api_view(['GET', 'POST'])
def games(request):
    if request.method == 'GET':
        query = Game.objects.filter(team1__lt=F('team2')).order_by('-date')
        serializer = GameResultSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def favorite_games(request):
    # user = request.query_params.get('user')
    if request.method == 'GET':
        user = request.user
        # if user.is_authenticated:
        down_side = datetime.now() - timedelta(days=1)
        up_side = datetime.now() + timedelta(days=1)
        favoriteGames = Game.objects.filter(releaseTime__gt=down_side, siteuser=user, releaseTime__lt=up_side)
        # favoriteGames =user.favoriteGames
        serializer = GameResultSerializer(favoriteGames, many=True)
        return Response(serializer.data)
    # else:
    #     return Response({})


@api_view(['GET', 'POST'])
def game_eventLine(request):
    team1 = request.query_params.get('team1')
    team2 = request.query_params.get('team2')
    date = request.query_params.get('date')
    if request.method == 'GET':
        game = Game.objects.filter(Q(team1__name=team1, team2__name=team2) | Q(team1__name=team2, team2__name=team1),
                                   date=date)[0]
        gameEvents = game.game_event_set
        serializer = GameEventSerializer(gameEvents, many=True)
        return Response(serializer.data)


class LeaguesListView(generics.ListAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueListSerializer


class LeagueDetailView(generics.ListAPIView):
    queryset = LeagueRow.objects.all()
    serializer_class = LeagueSerializer

    def get_queryset(self):
        return LeagueRow.objects.filter(league_id=self.kwargs['pk']).all()


@api_view(['GET', 'POST'])
def test(request):
    print("something")
    return Response(request.GET)
