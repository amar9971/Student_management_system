from django.shortcuts import render, redirect, HttpResponse
from api.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from api.models import user1


def base(request):
    return render(request, 'base.html')


def Login(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, 'email and password is invalid')
                return redirect('login')

        else:
            messages.error(request, 'email and password is invalid')
            return redirect('login')


def dologout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def profile(request):
    user = user1.objects.get(id=request.user.id)

    context = {
        "user": user,
    }

    return render(request, 'profile.html', context)

@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(profile_pic)

        try:
            customuser = user1.objects.get(id=request.user.id)
            customuser.profile_pic = profile_pic
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
                #customuser.save()
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request, 'Your Profile Does Not Updated !')

    return render(request,'profile.html')
