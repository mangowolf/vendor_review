# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import requests
import json
from .models import Company_Reviews, Company
from .forms import PostForm
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'review/index.html')

def registration(request):
    return render(request,'review/registration.html')

def new_company_review(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'review/new_company_review.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Company_Reviews, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'review/new_company_review.html', {'form': form})

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
'''
def company_review3(request):
    if request.method == "POST":
        form = Company_Reviews_Form(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
    else:
        form = Company_Reviews_Form()
    return render(request, 'review/company_review.html', {'form': form})
'''
def company_review(request):
    posts = Company_Reviews.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'review/company_review3.html',{'posts': posts})

def post_detail(request,pk):
    #Company_Reviews.objects.get(pk=pk)
    post = get_object_or_404(Company_Reviews, pk=pk)
    return render(request, 'review/post_detail.html', {'post': post})