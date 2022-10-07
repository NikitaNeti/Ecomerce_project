
# from http.client import HTTPResponse
from django.shortcuts import render, redirect ,HttpResponseRedirect
from Account.forms import SignupForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# def loginpage(request):
#     context={}
#     return render (request,'login.html',context)


def User_Register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        password = request.POST.get('password')
        if form.is_valid():
            user = form.save()
            user.set_password(password)
            user.save()
            login(request,user)
            messages.success(request,'Account Created Successfully !')

            return redirect('/')
        messages.success(request,'Unsuccessful Registration, Invalid information !')

    else:
        form = SignupForm()
    return render(request, 'templates/login.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            uemail = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
     
            user = authenticate(email= uemail,password=upass)
            if user is not None:
                login(request,user)
                return  HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request,'templates/login.html', {'form': fm})
    

def user_profile(request):
    return render(request,'templates/profile.html')





