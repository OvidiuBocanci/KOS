from django.contrib.auth.models import AbstractUser, User
from django.db import models

from class_schedule.models import ClassGym
from prices.models import Card


# Create your models here.

class UserSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    joined_classes = models.ForeignKey(ClassGym, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.user.first_name}"


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subscription = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    card_number = models.CharField(max_length=4)
    terms_and_conditions = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.subscription}'