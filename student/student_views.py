from django.shortcuts import render,redirect
from api.models import Student_notification , Student , Student_Feedback

def home(request):

    return render(request,'student/home.html')


def student_notification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id= i.id,
        notification = Student_notification.objects.filter(student_id= student_id )

        context = {
            'notification': notification,
        }
    return render(request,'student/notification.html', context)


def student_notification_mark_as_done(request, status):
    notification = Student_notification.objects.get(id= status)
    notification.status = 1
    notification.save()

    return redirect('student_notification')


def student_feedback(request):

    return render(request,'student/feedback.html')


def student_feedback_save(request):

    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)
        feedbacks= Student_Feedback(
            student_id=student,
            feedback= feedback,
            feedback_reply = "",


        )
        feedbacks.save()
        return redirect('student_feedback')