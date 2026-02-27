from django.http.response import HttpResponse
from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse("This is home page")
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")
def contacts(request):
    return HttpResponse("This is contact page")
def home(request):
    return render(request, 'home.html')