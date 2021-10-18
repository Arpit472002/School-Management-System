from django.db.models import fields
from rest_framework import serializers
from .models import *

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=['id','first_name','last_name','email','gender','created_at']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=['id','name','email','address','created_at']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','course_name','created_at']
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subject_name','course_name','staff','created_at']
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','email','gender','course','address','created_at']

class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveReportStudent
        fields=['id','student_name','leave_date','leave_message','leave_status','created_at']
class LeaveReportStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeaveReportStaff
        fields=['id','staff_name','leave_date','leave_message','leave_status','created_at']
class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentFeedback
        fields=['id','student_name','course_name','subject_name','staff_name','feedback','created_at']

class StaffFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffFeedback
        fields=['id','staff_name','course_name','subject_name','feedback','created_at']

class AdminNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminNotification
        fields=['id','admin_name','send_to_staff','send_to_student','notice','created_at']

class StaffNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffNotification
        fields=['id','staff_name','send_to_student','notice','created_at']


