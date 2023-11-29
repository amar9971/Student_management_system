from django.shortcuts import render, redirect
from api.models import Staff, Staff_notification ,Staff_leave, Staff_Feedback ,Subject, Session_year, Student, Attendance,Attendance_report
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def home(request):
    return render(request, 'staff/home.html')


@login_required(login_url='/')
def notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_notification.objects.filter(staff_id=staff_id)

        context = {

            'notification': notification
        }
        return render(request, 'staff/notification.html', context)


@login_required(login_url='/')
def staff_notification_mark_as_done(request, status):
    notification = Staff_notification.objects.get(id=status)
    notification.status = 1
    notification.save()

    return redirect('notification')


@login_required(login_url='/')
def staff_apply_leave(request):
    staff = Staff.objects.filter(admin= request.user.id)
    for i in staff:
        staff_id= i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)

        context = {

            'staff_leave_history':staff_leave_history,
        }
        return render(request, 'staff/apply_leave.html', context)


@login_required(login_url='/')
def staff_apply_leave_save(request):
    if request.method == "POST":
        leave_date= request.POST.get('leave_date')
        leave_message= request.POST.get('leave_massage')
        staff = Staff.objects.get(admin=request.user.id)
        leave = Staff_leave(

            staff_id= staff,
            date=  leave_date,
            message= leave_message,

        )
        leave.save()
        messages.success(request,'Leave are Successfully apply')

        return redirect('staff_apply_leave')


def staff_feedback(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history':feedback_history,

    }

    return render(request,'staff/staff_feedback.html', context)


def staff_feedback_save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin= request.user.id)
        feedback = Staff_Feedback(

            staff_id= staff,
            feedback=feedback,
            feedback_reply= ""
        )
        feedback.save()

        return redirect( 'staff_feedback')


def staff_take_attendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff= staff_id)
    session_year = Session_year.objects.all()

    action= request.GET.get('action')
    get_session_year = None
    get_subject= None
    students = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id= request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id=subject_id )
            get_session_year = Session_year.objects.get(id=session_year_id)

            subject= Subject.objects.filter(id= subject_id)

            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id= student_id)
    context = {
        'subject' : subject,
        'session_year' : session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,

    }

    return render(request,'staff/take_attendance.html',context)


def staff_save_attendance(request):
    if request.method=='POST':
        subject_id= request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        students_id= request.POST.getlist('students_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_year.objects.get(id=session_year_id)

        attendance = Attendance(
            subject_id= get_subject,
            attendance_data = attendance_date,
            session_year_id = get_session_year,
        )
        attendance.save()

        for i in students_id:
            stud_id = i
            int_stud= int(stud_id)

            p_students= Student.objects.get(id= int_stud)

            attendance_report = Attendance_report(
                student_id=p_students,
                attendance_id =attendance
            )
            attendance_report.save()

            return redirect('staff_take_attendance')


def staff_view_attendance(request):
    staff_id = Staff.objects.get(admin= request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    session_year= Session_year.objects.all()

    action = request.GET.get('action')
    get_subject= None
    get_session_year= None
    attendance_date= None
    attendance_report= None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            attendance_date=request.POST.get('attendance_date')

            get_subject= Subject.objects.get(id=subject_id)
            get_session_year = Session_year.objects.get(id= session_year_id)
            attendance=  Attendance.objects.filter(subject_id= get_subject, attendance_data = attendance_date)
            for i in attendance:
                attendance_id= i.id,
                attendance_report = Attendance_report.objects.filter(attendance_id=attendance_id)


    context = {
        'subject': subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,


    }
    return render(request,'staff/view_attendance.html', context)


def staff_add_result(request):
    staff = Staff.objects.get(admin= request.user.id)

    subject = Subject.objects.filter(staff_id= staff)
    session_year = Session_year.objects.all()

    action = request.GET.get('action')

    contaxt = {

        'subject':subject,
        'session_year':session_year,
        'action':action,
    }
    return render(request,'staff/add_result.html', contaxt)