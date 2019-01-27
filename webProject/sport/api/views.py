from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'POST'])
def game_results(request, teamName):
    sortBy = request.query_params.get('sort')

    if request.method == 'GET':
        query = Game.objects.filter(Q(team1__name=teamName))
        if sortBy=="win":
            query=query.order_by().order_by('-status')[:10]
        elif sortBy=="loose":
            query=query.order_by().order_by('status')[:10]
        elif sortBy=="side":
            query=query.order_by().order_by('-team2_name')[:10]
        elif sortBy=="date":
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


class LeaguesListView(generics.ListAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


@api_view(['GET', 'POST'])
def player_season_detail(request, pid):
    print(type(pid))
    if request.method == 'GET':
        player = Profile.objects.get(pid=pid)
        if player.type == "footballist":
            details = player.footballseasondetail_set
            serializer = FootBallSeasonDetailSerializer(details, many=True)

        elif player.type == "basketbalist":
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
        gameReport = Game_Report.objects.get(game=game)
        report_serializer = GameReportSerializer(gameReport)

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

class LeagueDetailView(generics.ListAPIView):
    queryset = LeagueRow.objects.all()
    serializer_class = LeagueSerializer

    def get_queryset(self):
        return LeagueRow.objects.filter(league_id=self.request.pk).all()
