from django.contrib.auth.models import AbstractUser, User
from django.db import models

from class_schedule.models import ClassGym


# Create your models here.

class UserSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # joined_classes = models.ManyToManyField(ClassGym)
    joined_classes = models.ForeignKey(ClassGym, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.user.first_name}"
