from django.db import models
from django.db.models import Avg

from authentication.models import User


class Topic(models.Model):  # can create a User with reputation >= 1000 or staff
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def rating(self, ) -> float:
        return self.reviews.aggregate(Avg('rating')).get('rating__avg')


class Review(models.Model):
    all_points = (
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),)
    on = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255)
    rating = models.IntegerField(choices=all_points)
    advantages = models.CharField(max_length=255)
    disadvantages = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # likes = ''
    # dislikes = ''

    def __str__(self):
        return f'+: {self.advantages} \n -: {self.disadvantages}'


class Criterion(models.Model):
    all_points = (
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),

    )
    title = models.CharField(max_length=255)
    points = models.IntegerField(choices=all_points)
    review = models.ForeignKey(Review, null=True, blank=True, on_delete=models.SET_NULL, related_name='criterions')
