# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return render(request, 'review/index.html')

def registration(request):
    return render(request,'review/registration.html')

def new_company_review(request):
    return render(request, 'review/new_company_review.html')

def company_review2(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'review/company_review.html', {'data': parsedData})

def company_review(request):
    if request.method == "POST":
        form = Company_Reviews_Form(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
    else:
        form = Company_Reviews_Form()
    return render(request, 'review/company_review.html', {'form': form})