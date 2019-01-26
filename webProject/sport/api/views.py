from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'POST'])
def game_results(request, teamName):
    if request.method == 'GET':
        query = Game.objects.filter(Q(team1__name=teamName) | Q(team2__name=teamName))[:10]
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

class LeagueDetailView(generics.GenericAPIView):

    pass