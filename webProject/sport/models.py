from django.db import models

# Create your models here.


class Team(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    bio=models.TextField(max_length=500)

class New(models.Model):
    title=models.TextField(max_length=500)
    subtitle=models.TextField(max_length=500)
    image=models.ImageField(upload_to='assets/teams')

class Profile(models.Model):

    pid=models.IntegerField()
    name=models.CharField(max_length=20)
    bio=models.TextField(max_length=500)
    gender=models.CharField(max_length=5)
    image=models.ImageField(upload_to='assets/players')
    birthDay=models.DateField()
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    currentTeam=models.ForeignKey(Team,on_delete=models.CASCADE,null=True)
    national=models.CharField(max_length=20)
    rule=models.CharField(max_length=20)
    previousClub=models.CharField(max_length=20)
    squad=models.CharField(max_length=20)
    favarites=models.ManyToManyField(New)






class Game(models.Model):
    team1=models.ForeignKey(Team,related_name='home',on_delete=models.CASCADE)
    team2=models.ForeignKey(Team,related_name='guest',on_delete=models.CASCADE)
    date=models.DateField()
    status=models.IntegerField()
    team1_score=models.IntegerField()
    team2_score=models.IntegerField()
    team1_possession=models.IntegerField()
    team2_possession=models.IntegerField()
    team1_shots=models.IntegerField()
    team2_shots=models.IntegerField()
    team1_corner=models.IntegerField()
    team2_corner=models.IntegerField()


class Game_Player(models.Model):
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    playerNumber=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    changingTime=models.CharField(max_length=20)

class Game_Report(models.Model):
    game=models.ForeignKey(Game,on_delete=models.CASCADE,primary_key=True)
    last_report=models.TextField(max_length=500)

class Game_Event(models.Model):
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    time=models.DateTimeField()
    text=models.TextField()