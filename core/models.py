from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class People(models.Model):
    category = models.ForeignKey(Category, related_name='people', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
