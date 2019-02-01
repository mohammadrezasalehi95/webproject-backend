from django.contrib.auth.models import User
from django.utils import timezone
from model_utils import Choices
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser
from django.db import models

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Team(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to='assets/sport/team', null=True, default='default_team.jpg')


#
# class TeamGame(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     game = models.ForeignKey("Game", on_delete=models.CASCADE)
#     against = models.CharField(max_length=20)
#     date = models.DateField(blank=True)
#     status = models.IntegerField(blank=True)
#     score = models.IntegerField(blank=True)
#     point = models.IntegerField(default=0, blank=True)

class SiteUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='assets/sport/users', null=True, blank=True)
    favoriteNews = models.ManyToManyField("New", blank=True)
    favoriteGames = models.ManyToManyField("Game", blank=True)

    def __str__(self):
        return self.email

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class New(models.Model):
    title = models.TextField(max_length=500)
    subtitle = models.TextField(max_length=500)
    content = models.TextField(max_length=2000)
    releaseTime = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='assets/sport/news', null=True)
    source = models.CharField(max_length=20, null=True)
    relateds = models.ManyToManyField("New", blank=True)
    media = models.FileField(upload_to='assets/sport/news', null=True, blank=True)
    likes = models.IntegerField(blank=True, default=0)


class Comment(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500)


class Profile(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=500)
    gender = models.CharField(max_length=5)
    image = models.ImageField(upload_to='assets/sport/players', null=True)
    born = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    currentTeam = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    national = models.CharField(max_length=20, null=True)
    rule = models.CharField(max_length=20, null=True)
    previousClub = models.CharField(max_length=20, null=True)
    squad = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=20, null=True, choices=(('F', 'FootBall'), ('B', 'BasketBall')))


class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name='home', on_delete=models.SET_NULL, null=True)
    team2 = models.ForeignKey(Team, related_name='guest', on_delete=models.SET_NULL, null=True)
    date = models.DateField(blank=True, default=timezone.now, null=True)
    status = models.IntegerField(blank=True, default=2, null=True)
    team1_score = models.IntegerField(blank=True, default=1, null=True)
    team2_score = models.IntegerField(blank=True, default=1, null=True)
    team1_point = models.IntegerField(default=0, blank=True, null=True)
    team2_point = models.IntegerField(default=0, blank=True, null=True)
    type = models.CharField(max_length=20, null=True, choices=(('F', 'FootBall'), ('B', 'BasketBall')))
    bestPlayer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    news = models.ManyToManyField(to=New)
    media1 = models.FileField(upload_to='assets/sport/games', null=True, blank=True)
    media2 = models.FileField(upload_to='assets/sport/games', null=True, blank=True)
    likes = models.IntegerField(blank=True, default=0)
    competition=models.ForeignKey('Competition',on_delete=models.CASCADE)


class GameSpecialDetail(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team1 = models.IntegerField(blank=True)
    team2 = models.IntegerField(blank=True)
    title = models.CharField(max_length=20, null=True)


class Game_Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    pid = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    post = models.CharField(max_length=20, blank=True)
    changingTime = models.CharField(max_length=20, blank=True)
    playTime = models.IntegerField(blank=True)


class Game_Report(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True)
    last_report = models.TextField(max_length=500)


class Game_Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)
    text = models.TextField(blank=True)


class Competition(models.Model):
    name = models.CharField(max_length=20,primary_key=True )
    type = Choices('League', 'Cup')
    field = models.CharField(max_length=1, choices=(('F', 'FootBall'), ('B', 'BasketBall')))
    current = models.BooleanField(default=True)
    image = models.ImageField(upload_to='assets/sport/competition', blank=True, null=True)


class Cup(Competition):
    team_number = models.IntegerField(choices=((4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)),
                                     default=16,
                                     null=True,
                                     blank=True)


class League(Competition):
    team_number = models.IntegerField(null=True, blank=True)


class LeagueRow(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    finished_game = models.IntegerField(blank=True)
    win = models.IntegerField(blank=True)
    lose = models.IntegerField(blank=True)
    equal = models.IntegerField(blank=True)
    point = models.IntegerField(blank=True)
    gf = models.IntegerField(blank=True)
    ga = models.IntegerField(blank=True)  # recieved goal

    def different_goal(self):
        return self.gf - self.ga


class FootBallSeasonDetail(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    season = models.CharField(max_length=20, blank=True, null=True)
    goals = models.IntegerField(null=True, blank=True)
    goalPass = models.IntegerField(null=True, blank=True)
    cards = models.IntegerField(null=True, blank=True)


class BasketSeasonDetail(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    season = models.CharField(max_length=20)
    twoscoreGoals = models.IntegerField(null=True, blank=True)
    threescoreGoals = models.IntegerField(null=True, blank=True)
    fault = models.IntegerField(null=True, blank=True)
    ribsndhs = models.IntegerField(null=True, blank=True)
    playTime = models.IntegerField(null=True, blank=True)
