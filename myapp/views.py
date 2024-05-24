from django.shortcuts import render, redirect
from django.contrib.auth .models import User, auth

from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username is already Exist !')
                return redirect('login')

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, ' Your Register Unsuccessfull !')
                return redirect('register')
    else:
        print("This is not Post Method")
    return render(request, 'register.html')




def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfull Your Logined !')
            return redirect('home')

        else:
            messages.error(request, 'Username Or Password is  invalid !')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Successfull Your Logout !')
    # return redirect('logout')
    return render(request, 'logout.html')
