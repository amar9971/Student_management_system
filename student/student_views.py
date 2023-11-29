from django.shortcuts import render, redirect
from api.models import Student_notification, Student, Student_Feedback, Student_leave, Subject, Attendance_report, \
    Attendance
from django.contrib import messages


def home(request):
    return render(request, 'student/home.html')


def student_notification(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id,
        notification = Student_notification.objects.filter(student_id=student_id)

        context = {
            'notification': notification,
        }
    return render(request, 'student/notification.html', context)


def student_notification_mark_as_done(request, status):
    notification = Student_notification.objects.get(id=status)
    notification.status = 1
    notification.save()

    return redirect('student_notification')


def student_feedback(request):
    return render(request, 'student/feedback.html')


def student_feedback_save(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)
        feedbacks = Student_Feedback(
            student_id=student,
            feedback=feedback,
            feedback_reply="",

        )
        feedbacks.save()
        return redirect('student_feedback')


def apply_for_leave(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id=student)

    context = {

        'student_leave_history': student_leave_history,
    }
    return render(request, 'student/student_leave.html', context)


def student_leave_save(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('message')
        student_id = Student.objects.get(admin=request.user.id)

        student_leave = Student_leave(
            student_id=student_id,
            date=leave_date,
            message=leave_message,
        )
        student_leave.save()
        messages.success(request, 'Leave are successfully send')
        return redirect('student_apply_for_leave')


def student_view_attendance(request):
    student = Student.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(course=student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)

            attendance_report = Attendance_report.objects.filter(student_id=student,
                                                                 attendance_id__subject_id=subject_id)

    context = {
        'subject': subject,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }

    return render(request, 'student/student_view_attendance.html', context)
