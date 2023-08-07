from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)

class TeacherModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    number=models.IntegerField()
    img=models.ImageField(upload_to='image/',null=True)
    Join_Date=models.DateField(auto_now_add=True)

class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    First_name=models.CharField(max_length=70)
    Last_name=models.CharField(max_length=70)
    Email=models.CharField(max_length=70)
    number=models.IntegerField()
    img=models.ImageField(upload_to='image/',null=True)
    Join_Date=models.DateField(auto_now_add=True)    