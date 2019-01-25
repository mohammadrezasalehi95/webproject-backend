from django.db import models

# Create your models here.


class Team(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    bio=models.TextField(max_length=500)


class Person(models.Model):

    pid=models.IntegerField()
    name=models.CharField(max_length=20)
    bio=models.TextField(max_length=500)
    gender=models.CharField(max_length=5)
    image=models.ImageField(upload_to='assets/')
    birthDay=models.DateField()
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    currentTeam=models.ForeignKey(Team,on_delete=models.CASCADE,to_field=name)
    national=models.CharField(max_length=20)
    rule=models.CharField(max_length=20)



class New(models.Model):
    title=models.TextField(max_length=500)
    subtitle=models.TextField(max_length=500)



