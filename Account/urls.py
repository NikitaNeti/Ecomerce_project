from django.urls import path
from Account import views

urlpatterns=[

    path('signup/',views.User_Register,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile ,name='profile')


]