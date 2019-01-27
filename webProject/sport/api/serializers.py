from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from ..models import *
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "date_joined")

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return super(UserRegistrationSerializer, self).create(validated_data)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return attrs


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GameResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class MemberTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'born', 'rule', 'squad', 'previousClub', 'image')


class LeagueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class FootBallSeasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootBallSeasonDetail
        exclude = ('profile',)


class BasketSeasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketSeasonDetail
        exclude = ('profile',)


class GameSpecialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSpecialDetail
        fields = '__all__'


class GameMembersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Player
        fields = '__all__'

class GameReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Report
        exclude = ('game',)
class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Event
        exclude = ('game',)

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeagueRow
        fields='__all__'
