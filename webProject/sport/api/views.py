from django.contrib.auth.models import User, Group
from django.db.models import Q
from rest_framework import viewsets
from ..models import *


from .serializers import UserSerializer, GroupSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class GameResults(viewsets.ModelViewSet):
    def get_queryset(self):
        teamName=self.kwargs['teamName']
        return Game.objects.filter(Q(team1=teamName) | Q(team2=teamName))[:10]

