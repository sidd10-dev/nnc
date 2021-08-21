from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login,logout,authenticate
from django.urls.base import reverse
from .models import customer
from .forms import *

def signup(request):
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        customerform = CustomerForm(data=request.POST)
        error = False

        if userform.is_valid() and customerform.is_valid():



            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            pass1 = userform.cleaned_data['password1']
            pass2 = userform.cleaned_data['password2']


            user = User(username = username, email = email, password = pass1)
            user.save()


            if user.password == pass2:
                user.set_password(user.password)
                user.save()

            
                address = customerform.cleaned_data['address']
                phone_no = customerform.cleaned_data['phone_no']

                cust = customer(address = address, phone_no = phone_no,user = user)
                cust.save()



            else:
                print("Passwords don't match")
            
            return HttpResponseRedirect(reverse_lazy('accounts:userlogin'))


        else:
            error = True
            return render(request, 'signup.html',{
                'userform': userform,
                'customerform': customerform,
                'error':error,
                'usererror':userform.errors,
                'customererror':customerform.errors
            })
    
    else:
        userform = UserForm()
        customerform = CustomerForm()
        return render(request, 'signup.html',{
            'userform': userform,
            'customerform': customerform,
        })

def userlogin(request):

    if request.method == 'POST':

        userform = Loginform(data=request.POST)

        if userform.is_valid():
            
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user:

                if user.is_active:

                    auth_login(request,user)
                    return redirect('nnc:home')

                else:
                    return HttpResponse("Your account is not active!.. Create a new account")

        else:
            return HttpResponse("Invalid Login Creds!")

    
    else:
        form = Loginform()
        return render(request,'login.html',{'form':form})









