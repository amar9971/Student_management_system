from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_views, staff_views, student_views
urlpatterns = [
    path('', views.Login, name='login'),
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('dologin/', views.dologin, name='dologin'),
    path('dologout', views.dologout, name='logout'),

    # this is hod panel url
    path('Hod/home', Hod_views.home, name='hod_home'),
    path('Hod/student/add',Hod_views.add_student, name='add_student'),
    path('Hod/student/view',Hod_views.view_student, name='view_student'),
    path('Hod/student/edit/<str:id>',Hod_views.edit_student, name = 'edit_student' ),
    path('Hod/student/update',Hod_views.update_student, name = 'update_student' ),

    path('Hod/student/delete/<str:admin>',Hod_views.delete_student, name = 'delete_student' ),

    path('Hod/course/add', Hod_views.add_course, name='add_course'),
    path('Hod/course/view', Hod_views.view_course, name='view_course'),
    path('Hod/course/edit/<str:id>', Hod_views.edit_course, name='edit_course'),
    path('Hod/course/update_course', Hod_views.update_course, name='update_course'),
    path('Hod/course/delete/<str:id>',Hod_views.delete_course, name = 'delete_course' ),

    path('profile', views.profile, name='profile'),

    path('profile/update', views.profile_update, name='profile_update'),

    #staff url

    path('Hod/staff/add', Hod_views.add_staff, name = 'add_staff'),
    path('Hod/staff/view', Hod_views.view_staff, name = 'view_staff'),
    path('Hod/staff/edit/<str:id>', Hod_views.edit_staff, name = 'edit_staff'),
    path('Hod/course/update_staff', Hod_views.update_staff, name='update_staff'),
    path('Hod/staff/delete/<str:admin>',Hod_views.delete_staff, name = 'delete_staff' ),

    #subject url

    path('Hod/subject/add',Hod_views.add_subject, name = 'add_subject'),
    path('Hod/subject/view',Hod_views.view_subject, name = 'view_subject'),
    path('Hod/subject/edit/<str:id>',Hod_views.edit_subject, name='edit_subject'),
    path('Hod/subject/update_subject', Hod_views.update_subject, name='update_subject'),
    path('Hod/subject/delete/<str:id>',Hod_views.delete_subject, name='delete_subject'),

    #sessions url
    path('Hod/session/add',Hod_views.add_session, name='add_session'),
    path('Hod/session/view',Hod_views.view_session, name='view_session'),
    path('Hod/session/edit<str:id>',Hod_views.edit_session, name='edit_session'),
    path('Hod/session/update_session',Hod_views.update_session, name='update_session'),
    path('Hod/session/delete/<str:id>',Hod_views.delete_session, name='delete_session'),

    path('Hod/staff/send_notification',Hod_views.staff_send_notification, name='staff_send_notification'),
    path('Hod/staff/save_notification',Hod_views.save_staff_notification, name='save_staff_notification'),

    path('Hod/staff/leave_view',Hod_views.staff_leave_view, name='staff_leave_view'),
    path('Hod/staff/approve_leave/<str:id>',Hod_views.staff_approve_leave, name='staff_approve_leave'),
    path('Hod/staff/disapprove_leave/<str:id>',Hod_views.staff_disapprove_leave, name='staff_disapprove_leave'),
    path('Hod/staff/feedback',Hod_views.staff_feedback, name='staff_feedback_reply'),
    path('Hod/staff/feedback/save',Hod_views.staff_feedback_save, name='staff_feedback_reply_save'),
    path('Hod/student/send_notification', Hod_views.student_send_notification, name = 'student_send_notification'),
    path('Hod/student/save_notification', Hod_views.save_student_notification, name = 'save_student_notification'),
    path('Hod/student/feedback',Hod_views.student_feedback, name='get_student_feedback'),

    path('Hod/student/feedback/reply/save',Hod_views.student_feedback_reply, name='reply_student_feedback'),
    path('Hod/student/leave_view',Hod_views.student_leave_view, name='student_leave_view'),
    path('Hod/student/approve_leave/<str:id>',Hod_views.student_approve_leave, name='student_approve_leave'),
    path('Hod/student/disapprove_leave/<str:id>',Hod_views.student_disapprove_leave, name='student_disapprove_leave'),
    path('Hod/view_attendance',Hod_views.hod_view_attendance, name='hod_view_attendance'),

    #staff panel url
    path('staff/home',staff_views.home, name='staff_home'),
    path('staff/notification',staff_views.notification, name='notification'),
    path('staff/mark_as_done/<str:status>',staff_views.staff_notification_mark_as_done, name='mark_as_done'),
    path('staff/apply_leave',staff_views.staff_apply_leave, name='staff_apply_leave'),
    path('staff/apply_leave_save',staff_views.staff_apply_leave_save, name='staff_apply_leave_save'),
    path('staff/feedback',staff_views.staff_feedback, name='staff_feedback'),
    path('staff/feedback_save',staff_views.staff_feedback_save, name='staff_feedback_save'),
    path('staff/take_attendance',staff_views.staff_take_attendance, name='staff_take_attendance'),
    path('staff/save_attendance',staff_views.staff_save_attendance, name='staff_save_attendance'),
    path('staff/view_attendance',staff_views.staff_view_attendance, name='staff_view_attendance'),
    path('staff/add/result',staff_views.staff_add_result, name='staff_add_result'),


    #student url
    path('student/home',student_views.home, name='student_home'),
    path('student/notification',student_views.student_notification, name='student_notification'),
    path('student/mark_as_done/<str:status>',student_views.student_notification_mark_as_done, name='student_mark_as_done'),
    path('student/feedback',student_views.student_feedback, name='student_feedback'),
    path('student/feedback_save',student_views.student_feedback_save, name='student_feedback_save'),
    path('student/apply_for_leave',student_views.apply_for_leave, name='student_apply_for_leave'),
    path('student/leave_save',student_views.student_leave_save, name='student_leave_save'),
    path('student/view_attendance',student_views.student_view_attendance, name='student_view_attendance'),


] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
