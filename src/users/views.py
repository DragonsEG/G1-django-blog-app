from django import forms
from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class registerform(forms.Form):
    first_name = forms.CharField(label="firstName")
    last_name = forms.CharField(label="lastName")
    email= forms.EmailField(label="email",widget=forms.EmailInput)
    username=forms.CharField(label="username")
    pass1 = forms.CharField(label="password",widget=forms.PasswordInput)
    pass2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=User.UserGroups.choices)
class loginform(forms.Form):

    email = forms.EmailField(label="Email",required=True,widget=forms.EmailInput)
    password = forms.CharField(label="password",widget=forms.PasswordInput)

def Login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('/admin')
            return redirect('login')
    form = loginform()
    return render(request, 'login.html',{'form':form})

def Logout(request):
    logout(request)

    return redirect('/login')

def Register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['pass1'] == cd['pass2']:
                user = User.objects.create_user(
                    username=cd['username'],
                    email=cd['email'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    user_group= cd['group'],
                    password=cd['pass1']
                )
                return redirect('login')

    form = registerform()

    return render(request, 'register.html', {'form': form})