from django.shortcuts import render
from django.http import HttpResponse
from flatpages import views
def home(request):
    return render(request, 'templates/static_handler.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!')

# Create your views here.
