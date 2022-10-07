from django.urls import path
from Product.views import *

urlpatterns=[
    path('',index),

    # path('product-detail/<int:pk>',views.views.product_detail,name='product_detail'),
    ]