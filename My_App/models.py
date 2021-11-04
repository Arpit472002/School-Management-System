from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.manager import Manager
# Create your models here.
STUDENT_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
HOD_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
STAFF_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')    
)
REGISTRATION_GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others') 
)
POST_CHOICES=(
    ('HOD','HOD'),
    ('Staff','Staff'),
    ('Student','Student')
)
class MyUser(AbstractUser):
    gender=models.CharField(max_length=200,choices=REGISTRATION_GENDER)
    post=models.CharField(max_length=200,choices=POST_CHOICES)
    phone_number=models.CharField(max_length=10)

class HOD(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=200,choices=HOD_GENDER)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.OneToOneField(MyUser,on_delete=models.CASCADE)
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
    user_name=models.OneToOneField(MyUser,on_delete=models.CASCADE)
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

class HODNotification(models.Model):
    HOD_name=models.ForeignKey(HOD,on_delete=models.CASCADE)
    send_to_staff=models.ManyToManyField(Staff)
    send_to_student=models.ManyToManyField(Student)
    notice=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.HOD_name

class StaffNotification(models.Model):
    staff_name=models.ForeignKey(Staff,on_delete=models.CASCADE)
    send_to_student=models.ManyToManyField(Student)
    notice=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.staff_name)


