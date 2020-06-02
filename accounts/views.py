from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.


def web(request):
    return HttpResponse(request, 'www.Travello.com')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def aboutus(request):
    return render(request, 'about.html')


def index(request):
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'msg': 'User Name has been Taken'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'msg': 'Email has been used'})
        elif password2 != password1:
            return render(request, 'register.html', {'msg': 'password Doesn\'t match'})
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password2)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if request.POST['adminr'] is 'on':
                return render(request, 'login.html', {'msg': 'You can not select both'})
            elif request.POST['userr'] is 'on':
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'login.html', {'msg': 'Could not found'})
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_superuser:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'login.html', {'msg': 'Admin id could not found'})
        return render(request, 'login.html')
    except 'null':
        print('null')


def logout(request):
    auth.logout(request)
    print(request)
    return redirect('/')
