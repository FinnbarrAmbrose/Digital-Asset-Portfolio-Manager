from django.shortcuts import render
from django.http import HttpResponse

def my_digital_asset(request):
    return HttpResponse("Hello, digital assets!")

