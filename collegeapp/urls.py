from django.urls import path
from collegeapp import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('adminhomepage',views.adminhomepage,name='adminhomepage'),
   path('teacherhomepage',views.teacherhomepage,name='teacherhomepage'),
   path('registerpage',views.registerpage,name='registerpage'),
   path('coursepage',views.coursepage,name='coursepage'),
   path('addcourse',views.addcourse,name='addcourse'),
   path('teacherreg',views.teacherreg,name='teacherreg'),
   path('studentpage',views.studentpage,name='studentpage'),
   path('addstudent',views.addstudent,name='addstudent'),
   path('teacherdetail',views.teacherdetail,name='teacherdetail'),
   path('log',views.log,name='log'),
   path('loginpage',views.loginpage,name='loginpage'),
   path('sdetails',views.sdetails,name='sdetails'),
   path('tcard/<int:tid>',views.tcard,name='tcard'),
   path('scard/<int:sid>',views.scard,name='scard'),
   path('editpage/<int:tid>',views.editpage,name='editpage'),
   path('edit_details/<int:tid>',views.edit_details,name='edit_details'),
   path('editstudentpage/<int:tid>',views.editstudentpage,name='editstudentpage'),
   path('edit_studentdetails/<int:tid>',views.edit_studentdetails,name='edit_studentdetails'),
   path('delete_teacher/<int:tid>',views.delete_teacher,name='delete_teacher'),
   path('delete_student/<int:tid>',views.delete_student,name='delete_student'),
   path('logout',views.logout,name='logout'),
   
]
