from django.db import models

# Create your models here.

class Member(models.Model):

    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    gender = models.CharField(choices=gender_options, max_length=6)
    profile = models.ImageField(upload_to='profile_members/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'