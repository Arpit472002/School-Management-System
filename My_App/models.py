from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractUser
# Create your models here.
STUDENT_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
ADMIN_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
STAFF_GENDER=(
    ('Male','Male'),
    ('Male','Female'),
    ('Others','Others')    
)


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=200,choices=ADMIN_GENDER)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=200,choices=STAFF_GENDER)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course_name

class Subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=200)
    course_name=models.ManyToManyField(Course)
    staff=models.ManyToManyField(Staff)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject_name

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=200,choices=STUDENT_GENDER)
    course=models.ManyToManyField(Course)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    leave_date=models.DateField()
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name

class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date=models.DateField()
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_name
class StudentFeedback(models.Model):
    id=models.AutoField(primary_key=True)
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    subject_name=models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)
    staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE,blank=True,null=True)
    feedback=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name

class StaffFeedback(models.Model):
    id=models.AutoField(primary_key=True)
    staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    subject_name=models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)
    feedback=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_name

class AdminNotification(models.Model):
    admin_name=models.ForeignKey(Admin,on_delete=models.CASCADE)
    send_to_staff=models.ManyToManyField(Staff)
    send_to_student=models.ManyToManyField(Student)
    notice=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.admin_name

class StaffNotification(models.Model):
    staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE)
    send_to_student=models.ManyToManyField(Student)
    notice=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.staff_name



from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)