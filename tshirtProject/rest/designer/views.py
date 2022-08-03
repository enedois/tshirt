from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse('This is index of Tshirt Printing Company')
     return render(request, 'designer.html')
