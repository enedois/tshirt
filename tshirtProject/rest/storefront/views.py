from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the storefront page of Tshirt Printing Company')    
    #return render(request, 'storefront.html')
# Create your views here.
