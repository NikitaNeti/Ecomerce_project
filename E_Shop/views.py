from multiprocessing import context
from urllib import request
from django.shortcuts import render

# Create your views here.

def home(request):
    context ={}
    return render(request,'index.html',context)
