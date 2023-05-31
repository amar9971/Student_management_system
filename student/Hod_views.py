from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Course, Session_year


@login_required(login_url='/')
def home(request):
    return render(request, 'Hod/home.html')


#@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year= Session_year.objects.all()

    if request.method == "POST":
        profile_pic = request.POST.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        print(gender)
    context = {
        'course': course,
        'session_year': session_year,
    }


    return render(request, 'Hod/add_student.html', context)

