from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class PlayerStatus(Enum):
    STUDENT = "Student"
    VOLUNTEER = "Volunteer"


class GameResult(Enum):
    WHITE_WIN = "White Win"
    BLACK_WIN = "Black Win"
    DRAW = "Draw"
    STALEMATE = "Stalemate"
    UNKNOWN = "Unknown"
    BLANK = ""


class GameColor(Enum):
    WHITE = "White"
    BLACK = "Black"


class UserClub(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=False)


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[(tag.name, tag.value) for tag in PlayerStatus])
    old_rating = models.IntegerField(default=100)
    current_rating = models.IntegerField(default=100)
    starting_rating = models.IntegerField(default=100)
    opponent_one = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='opponent_one'
        )
    opponent_two = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='opponent_two'
        )
    opponent_three = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='opponent_three'
        )
    grade = models.CharField(max_length=100)
    parent_email = models.CharField(max_length=300)
    parent_name = models.CharField(max_length=100)
    parent_number = models.CharField(max_length=20)
    last_played = models.CharField(max_length=100, choices=[(tag.name, tag.value) for tag in GameColor])


class Class(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    teacher_main = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    teacher_secondary = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    club = models.ForeignKey(UserClub, on_delete=models.CASCADE, null=False, blank=False)


class Game(models.Model):
    board_letter = models.CharField(max_length=2)
    board_number = models.IntegerField()
    white_player = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, blank=False, related_name='playerW')
    black_player = models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, blank=False, related_name='playerB')
    result = models.CharField(max_length=100, choices=[(tag.name, tag.value) for tag in GameResult])


class UserGroupPlayer(models.Model):
    club = models.ForeignKey(UserClub, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)