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

    path('profile', views.profile, name='profile'),

    path('profile/update', views.profile_update, name='profile_update')



] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
