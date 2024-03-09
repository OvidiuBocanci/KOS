from urllib import request

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models




def logged_user(request):
        return request.user
from django.contrib.auth.decorators import login_required
class ClassGym(models.Model):

    class_option = {
        ('trx', 'Trx'),
        ('cycling', 'Cycling'),
        ('crossfit', 'Crossfit'),
        ('bodypump', 'Bodypump'),
        ('aerobic', 'Aerobic'),
        ('zumba', 'Zumba')
    }

    title = models.CharField(choices=class_option, max_length=8)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    people_nr = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.trainer}'