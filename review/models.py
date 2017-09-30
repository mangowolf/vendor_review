# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(default='noreply@example.com')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Company(models.Model):
    website = models.URLField()
    headquarters = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    revenue = models.IntegerField()
    size = models.IntegerField()
    founded = models.DateField()
    summary = models.TextField()

class Company_Reviews(models.Model):
    companykey = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        )
    metarating = models.DecimalField(max_digits=2, decimal_places=1)
    linkedin_icon = models.ImageField(height_field=100, width_field=100)
    linkedin_stars = models.DecimalField(max_digits=3, decimal_places=2)
    review_text = models.TextField(max_length=2000)
