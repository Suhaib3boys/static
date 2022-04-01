from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']
        check = auth.authenticate(username=user, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect('/')
        else:
            messages.info(request, 'Invalid User Name / Password ')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=user).exists():
                messages.info(request, 'User Name Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=user, email=email, password=password, first_name=name)
                new_user.save()
                messages.info(request, 'User Created')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
