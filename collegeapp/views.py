from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import*

def homepage(request):
    return render(request,"home.html")

def adminhomepage(request):
    return render(request,"adminhome.html")
def teacherhomepage(request):
        current_user=request.user
        uid=current_user.id
        print(uid)
        teacher=TeacherModel.objects.get(user=uid)
        return render(request,"thome.html",{'teacher':teacher})

def adminhomepage(request):
    return render(request,"adminhome.html")

def coursepage(request):
    return render(request,"course.html")

def addcourse(request):
    if request.method == 'POST':
        course=request.POST['cname']
        data = CourseModel(Course_Name=course)
        data.save()
        return redirect('adminhomepage')


def registerpage(request):
    course=CourseModel.objects.all()
    context={'course':course}
    return render(request,"reg.html",context)

def teacherreg(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        usname=request.POST['uname']
        num=request.POST['ph']
        pswd=request.POST['pass']
        cpswd=request.POST['cpass']
        cselete=request.POST['select']
        img=request.FILES.get('file')
        course=CourseModel.objects.get(id=cselete)

        if pswd==cpswd:
            if User.objects.filter(username=usname).exists():
                return redirect('registerpage')
            elif User.objects.filter(email=email).exists():
                return redirect('registerpage')
            else:
                user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=usname,password=pswd)
                user.save()
                data=User.objects.get(id=user.id)
                teacher=TeacherModel(number=num,img=img,Course=course,user=data)
                teacher.save()
                print("success")
                return redirect('log')

        else:
            print("password error")
            return redirect('registerpage')

    else:
            print(" error")
            return redirect('registerpage')

def studentpage(request):
    course=CourseModel.objects.all()
    context={'course':course}
    return render(request,"student.html",context)

def addstudent(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        num=request.POST['ph']
        cselete=request.POST['select']
        img=request.FILES.get('file')
        course=CourseModel.objects.get(id=cselete)
        student=StudentModel(First_name=fn,Last_name=ln,Email=email,number=num,img=img,Course=course)
        student.save()
        print("add student")
        return redirect('sdetails')
    else:
        return redirect('studentpage')
    
def log(request):
    return render(request,"login.html")    

def loginpage(request):
    if request.method=='POST':
        username = request.POST['ui']
        password = request.POST['pa']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            if request.user.is_staff==1:
                print("admin")
                
                return redirect('adminhomepage')
                 
            else:
              
              print("thome")
              return redirect('teacherhomepage')
              
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            print("try again")
            return redirect('log')
    else:
        print("try again")
        return redirect('log')

def sdetails(request):
    students=StudentModel.objects.all()
    return render(request,'studentdetails.html',{'students':students})
def teacherdetail(request):
        teacher=TeacherModel.objects.all()
       
        return render(request,"teacherdetails.html",{'teacher':teacher})
def tcard(request,tid):
        teacher=TeacherModel.objects.get(id=tid)
       
        return render(request,"teachercard.html",{'teacher':teacher})

def scard(request,sid):
        student=StudentModel.objects.get(id=sid)
       
        return render(request,"studentcard.html",{'student':student})



def editpage(request,tid):
    teacher=TeacherModel.objects.get(id=tid)
   
    context={'teacher':teacher}
    
    return render(request,'edit.html',context)

def edit_details(request,tid):
    if request.method=='POST':
        teacher=TeacherModel.objects.get(id=tid)
        old=teacher.img
        new=request.FILES.get('file')
        if old!=None and new==None:
            teacher.img=old
        else:
            teacher.img=new
        
        teacher.user.first_name=request.POST.get('fname')
        teacher.user.last_name=request.POST.get('lname')
        teacher.user.email=request.POST.get('eid')
        teacher.user.username=request.POST.get('uname')
        teacher.number=request.POST.get('ph')
        select=request.POST.get('select')
        course=CourseModel.objects.get(id=select)
        teacher.Course=course
        teacher.save()
        teacher.user.save()
        print("update success")
        
        if request.user.is_staff==1:
            print("admin")
                
            return redirect('teacherdetail')
                 
        else:
              
            print("thome")
            return redirect('teacherhomepage')
       
              
        
    return request(request,"edit.html")

def editstudentpage(request,tid):
    student=StudentModel.objects.get(id=tid)
    context={'student':student}
    
    return render(request,'editstudent.html',context)

def edit_studentdetails(request,tid):
    if request.method=='POST':
        student=StudentModel.objects.get(id=tid)
        old=student.img
        new=request.FILES.get('file')
        if old!=None and new==None:
            student.img=old
        else:
            student.img=new
        
        student.First_name=request.POST.get('fname')
        student.Last_name=request.POST.get('lname')
        student.Email=request.POST.get('eid')
        student.number=request.POST.get('ph')
        select=request.POST.get('select')
        course=CourseModel.objects.get(id=select)
        student.Course=course
        student.save()
        print("update success")
        return redirect('adminhomepage')
    return request(request,"editstudent.html")

def delete_teacher(request,tid):
    teacher=TeacherModel.objects.get(id=tid)
    teacher.delete()
    if request.user.is_staff==1:
        print("admin")
                
        return redirect('teacherdetail')
                 
    else:
              
        print("thome")
        return redirect('homepage')

def delete_student(request,tid):
    teacher=StudentModel.objects.get(id=tid)
    teacher.delete()
    print("delete product")
    return redirect('sdetails')

def logout(request):
	auth.logout(request)
	return redirect('homepage')