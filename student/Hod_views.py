from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Course, Session_year, user1, Student, Staff, Subject
from django.contrib import messages


@login_required(login_url='/')
def home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count= Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender= 'Male').count()
    student_gender_female = Student.objects.filter(gender= 'Female').count()

    context = {
        'student_count':student_count,
        'staff_count': staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }
    return render(request, 'Hod/home.html', context)


@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        if user1.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')

        if user1.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')
        else:
            user = user1(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                course_id=course,
                session_year_id=session_year,
                gender=gender
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + "Are Successfully Added")
            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def view_student(request):
    student = Student.objects.all()
    context = {

        'student': student,
    }
    return render(request, 'Hod/view_student.html', context)


@login_required(login_url='/')
def edit_student(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_year.objects.all()

    context = {

        'student': student,
        'course': course,
        'session_year': session_year
    }
    return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        user = user1.objects.get(id=student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
            # customuser.save()
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course_id)
        student.course_id = course

        session_year = Session_year.objects.get(id=session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Record are successfully updated ')
        return redirect('view_student')

    return render(request, 'Hod/edit_student.html')


@login_required(login_url='/')
def delete_student(request, admin):
    student = user1.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Record are successfully delete')
    return redirect('view_student')


@login_required(login_url='/')
def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name=course_name
        )
        course.save()
        messages.success(request, 'Course are successfully created')
        return redirect('add_course')

    return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def view_course(request):
    course = Course.objects.all()

    context = {
        'course': course,
    }
    return render(request, 'Hod/view_course.html', context)


@login_required(login_url='/')
def edit_course(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, 'Hod/edit_course.html', context)


@login_required(login_url='/')
def update_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course are successfully updated !')
        return redirect('view_course')
    return render(request, 'Hod/edit_course.html', )


@login_required(login_url='/')
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are successfully delete')
    return redirect('view_course')


@login_required(login_url='/')
def add_staff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if user1.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken !')
            return redirect('add_staff')

        if user1.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken !')
            return redirect('add_staff')

        else:
            user = user1(
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type=2,
                username=username,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                gender=gender,
                address=address,
            )
            staff.save()
            messages.success(request, 'Staff are successfully add !')
            return redirect('add_staff')
    return render(request, 'Hod/add_staff.html')


@login_required(login_url='/')
def view_staff(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff
    }
    return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def edit_staff(request, id):
    staff = Staff.objects.get(id=id)
    context = {

        'staff': staff
    }

    return render(request, 'Hod/edit_staff.html', context)


@login_required(login_url='/')
def update_staff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        user = user1.objects.get(id=staff_id)
        user.username = username

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
            # customuser.save()
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request, 'Staff are successfully updated !')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def delete_staff(request, admin):
    staff = user1.objects.get(id=admin)
    staff.delete()
    messages.success(request, ' Staff Record are successfully delete')
    return redirect('view_staff')


@login_required(login_url='/')
def add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request, 'Subject are sucessfully added !')
        return redirect('add_subject')

    context = {

        'course': course,
        'staff': staff,
    }
    return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def view_subject(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject
    }
    return render(request, 'Hod/view_subject.html', context)


def edit_subject(request, id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'course': course,
        'staff': staff

    }
    return render(request, 'Hod/edit_subject.html', context)


def update_subject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request, 'Subject are successfully updated !')
        return redirect('view_subject')


def delete_subject(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request, 'Subject are successfully deleted !')

    return redirect('view_subject')


def add_session(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_year (
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session are successfully  created !')
        return redirect('add_session')

    return render(request, 'Hod/add_session.html')


def view_session(request):
    session = Session_year.objects.all()
    context = {
        'session': session
    }
    return render(request,'Hod/view_session.html', context)


def edit_session(request, id):
    session = Session_year.objects.filter(id=id)
    context = {
        'session':session
    }
    return render(request,'Hod/edit_session.html', context)


def update_session(request):
    if request.method=="POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,'session are successfully updated !')

    return redirect('view_session')


def delete_session(request, id ):
    session = Session_year.objects.get(id=id)
    session.delete()
    messages.success(request, 'Session year  are successfully deleted !')

    return redirect('view_session')


def staff_send_notification(request):
    return render(request, 'Hod/send_staff_notification.html')