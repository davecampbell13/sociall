from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the users index.")