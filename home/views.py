from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')


# def index(request):
# return HttpResponse('hello world')