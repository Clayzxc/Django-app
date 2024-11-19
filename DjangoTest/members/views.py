from django.template import loader
from .models import Member
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render({}, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

def login_user(request):
  template = loader.get_template('authenticate/login.html')
  if request.method == 'POST':
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.success(request, 'There Was An Error Logging In, Try Again...')
      return redirect('/login')
  else:
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
  logout(request)
  return redirect('/')

def signup_user(request):
  template = loader.get_template('authenticate/signup.html')
  if request.method == 'POST':
    username = request.POST["username"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    if User.objects.filter(username=username).exists():
      messages.success(request, "User already exists...")
      return redirect('/signup')
    elif password1 != password2:
      messages.success(request, "Password don't match...")
      return redirect('/signup')
    else:
      create_user = User.objects.create_user(username=f"{username}", password=f"{password1}")
      create_user.save()
      user = authenticate(request, username=username, password=password1)
      if user is not None:
        login(request, user)
        return redirect('/')
  else:
    return render(request, 'authenticate/signup.html', {})

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render({}, request))

def user_info(request):
  template = loader.get_template('user/user_info.html')
  return HttpResponse(template.render({}, request))

def custom_404(request):
  template = loader.get_template('404.html')
  return HttpResponse(template.render({}, request))