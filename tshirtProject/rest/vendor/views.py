from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the vendor page of Tshirt Printing Company')    

# Create your views here.
