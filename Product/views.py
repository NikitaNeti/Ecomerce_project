from django.shortcuts import render
from Product.models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()    
    return render(request,'templates/index.html',{'categories':categories})


def product_detail(request):
    return render(request,'product-details.html')
