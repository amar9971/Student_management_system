from django.shortcuts import render, redirect
from api.models import Staff, Staff_notification ,Staff_leave, Staff_Feedback
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