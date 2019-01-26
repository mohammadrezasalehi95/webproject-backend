from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Team(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to='assets/sport/team', null=True, default='default_team.jpg')


class New(models.Model):
    title = models.TextField(max_length=500)
    subtitle = models.TextField(max_length=500)
    image = models.ImageField(upload_to='assets/sport/news', null=True)


class Profile(models.Model):
    pid=models.IntegerField()
    name=models.CharField(max_length=20)
    bio=models.TextField(max_length=500)
    gender=models.CharField(max_length=5)
    image=models.ImageField(upload_to='assets/sport/players',null=True)
    born=models.DateField()
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    currentTeam=models.ForeignKey(Team,on_delete=models.CASCADE,null=True)
    national=models.CharField(max_length=20)
    rule=models.CharField(max_length=20)
    previousClub=models.CharField(max_length=20,null=True)
    squad=models.CharField(max_length=20,null=True)
    type=models.CharField(max_length=20,null=True)

class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name='home', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='guest', on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    status = models.IntegerField(blank=True)
    team1_score = models.IntegerField(blank=True)
    team2_score = models.IntegerField(blank=True)
    team1_possession = models.IntegerField(blank=True)
    team2_possession = models.IntegerField(blank=True)
    team1_shots = models.IntegerField(blank=True)
    team2_shots = models.IntegerField(blank=True)
    team1_corner = models.IntegerField(blank=True)
    team2_corner = models.IntegerField(blank=True)
    team1_point = models.IntegerField(default=0, blank=True)
    team2_point = models.IntegerField(default=0, blank=True)


class Game_Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    playerNumber = models.CharField(max_length=20, blank=True)
    post = models.CharField(max_length=20, blank=True)
    changingTime = models.CharField(max_length=20, blank=True)


class Game_Report(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    last_report = models.TextField(max_length=500)


class Game_Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)
    text = models.TextField(blank=True)


class Competition(models.Model):
    class Meta:
        abstract = True


class LeagueCompetition(models.Model):
    pass


class CupCompetition(models.Model):
    pass


class League(models.Model):
    type = models.CharField(max_length=1, choices=(('F', 'FootBall'), ('B', 'BaskerBall')))
    teams_number = models.IntegerField(blank=True)


class LeagueRow(models.Model):
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


class Cup(models.Model):
    type = models.IntegerField(choices=((4, 4), (8, 8), (16, 16), (32, 32), (64, 64), (128, 128)))


class FootBallSpringDetail(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    spring =models.CharField(max_length=20)
    goals=models.IntegerField(null=True)
    goalPass=models.IntegerField(null=True)
    cards =models.IntegerField(null=True)

class BasketSpringDetail(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    spring = models.CharField(max_length=20)
    twoscoreGoals=models.IntegerField(null=True)
    threescoreGoals=models.IntegerField(null=True)
    fault=models.IntegerField(null=True)
    ribsndhs=models.IntegerField(null=True)
    playTime= models.TimeField(null=True)
