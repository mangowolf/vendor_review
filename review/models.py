# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(default="company",max_length=255)
    website = models.URLField()
    headquarters = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    revenue = models.IntegerField()
    size = models.IntegerField()
    founded = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return self.company_name

class Company_Reviews(models.Model):
    companykey = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        )
    #metarating = models.DecimalField(max_digits=2, decimal_places=1)
    #linkedin_icon = models.ImageField(height_field=100, width_field=100)
    #linkedin_stars = models.DecimalField(max_digits=3, decimal_places=2)
    #review_text = models.TextField(max_length=2000)
    star_rating = models.PositiveSmallIntegerField(default='0')
    title = models.CharField(default='',max_length=300)
    review = models.TextField(default='')
    author = models.ForeignKey('auth.User',default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class Company_Reviews_Form(ModelForm):
#    class Meta:
#        model = Company_Reviews
#        fields = ['star_rating', 'company_name', 'review']

#form = Company_Reviews_Form()
#review = Company_Reviews.objects.get(pk=1)
#form = Company_Reviews_Form(instance=review)