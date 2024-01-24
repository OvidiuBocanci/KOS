from django.db import models

# Create your models here.

class Card(models.Model):

    title = models.CharField(max_length=50)
    title_detail = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    price_detail = models.CharField(max_length=50)
    benefit_1 = models.CharField(max_length=50, blank=True)
    benefit_2 = models.CharField(max_length=50, blank=True)
    benefit_3 = models.CharField(max_length=50, blank=True)
    benefit_4 = models.CharField(max_length=50, blank=True)
    benefit_5 = models.CharField(max_length=50, blank=True)
    benefit_6 = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.price}'