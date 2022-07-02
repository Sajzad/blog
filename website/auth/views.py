import json, re

from django.shortcuts import render, redirect, reverse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def client_signup_view(request):

    errors = []
    message = ''

    if request.method == "POST":
        print("signup")
        data = json.loads(request.body)
        username = data.get("username")
        first_name = data.get("f_name")
        last_name = data.get("l_name")
        email = data.get("email")
        password = data.get("password")

        if username:
            if User.objects.filter(username=username).exists():
                error = {"error": "This Username Already exists"}
                errors.append(error)
        else:
            error = {"error": "Please provide Username"}
            errors.append(error)

        if not first_name:
            error = {"error": "Please provide First Name"}
            errors.append(error)

        if not last_name:
            error = {"error": "Please provide Last Name"}
            errors.append(error)
        
        if email:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.fullmatch(regex, email):
                error = {"error": "Email is not valid"}
                errors.append(error)
            
            elif User.objects.filter(email=email).exists():
                error = {"error": "This Email already exists"}
                errors.append(error)
        else:
            error = {"error": "Please provide Email"}
            errors.append(error)

        if password:
            if len(password)<6:
                error = {"error": "Password must be at least 6 characters"}
                errors.append(error)

        if not errors:
            User.objects.create_user(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            message = "Account created Succesfully"
        print(errors)
        resp = {
            'errors': errors,
            'message': message
        }
        return JsonResponse(data=resp, status=200)

    return render(request, 'account/signup.html')

def client_signin_view(request):
    
    errors = []

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get("password")

        if not username:
            error = {"error": "Username can't be empty"}
            errors.append(error)
        if not password:
            error = {"error": "Password can't be empty"}
            errors.append(error)

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('base:home'))
            else:
                error = {"error": "Username/Password doesn't match"}
                errors.append(error)

    context = {
        'errors': errors
    }

    return render(request, 'account/signin.html', context)

def logout_view(request):
    logout(request)
    return redirect(reverse("base:home"))
