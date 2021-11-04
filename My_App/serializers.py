from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields='__all__'

class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model=HOD
        fields='__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'

        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    taken_by=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=Course
        fields=['id','course_name','taken_by','created_at']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subject_name','course_name','staff','created_at']


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

class HODNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=HODNotification
        fields=['id','HOD_name','send_to_staff','send_to_student','notice','created_at']

class StaffNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffNotification
        fields=['id','staff_name','send_to_student','notice','created_at']


