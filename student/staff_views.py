from django.shortcuts import render, redirect
from api.models import Staff, Staff_notification ,Staff_leave
from django.contrib import messages

def home(request):
    return render(request, 'staff/home.html')


def notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_notification.objects.filter(staff_id=staff_id)

        context = {

            'notification': notification
        }
        return render(request, 'staff/notification.html', context)


def staff_notification_mark_as_done(request, status):
    notification = Staff_notification.objects.get(id=status)
    notification.status = 1
    notification.save()

    return redirect('notification')


def staff_apply_leave(request):
    return render(request, 'staff/apply_leave.html')


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