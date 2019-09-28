from django.shortcuts import render
from django.http import HttpResponse



def index(request):

    return render(request,'home.html')


def about(request):

    return render(request,'about-cnt.html')

def software(request):

    return render(request,'software.html')

def cyber(request):

    return render(request,'cyber.html')
def cloud(request):

    return render(request,'cloud.html')
def digital(request):

    return render(request,'digital.html')

def datascience(request):

    return render(request,'datascience.html')

def testing(request):

    return render(request,'testing.html')


def development(request):

    return render(request,'developement.html')



def itconsultancy(request):

    return render(request,'it-consultancy.html')

def contact(request):

    return render(request,'contact.html')