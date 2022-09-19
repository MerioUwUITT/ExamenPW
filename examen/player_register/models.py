from django.db import models
class Position(models.Model):
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.position
class Stadium(models.Model):
    stadium = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.stadium
class Team(models.Model):
    team = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_drawn = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, default= 1)
    def __str__(self):
        return self.team + ' de ' + self.city
# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=2, max_digits=4)
    weight = models.DecimalField(decimal_places=2, max_digits=4)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default= 1)
    def __str__(self):
        return self.name



    
