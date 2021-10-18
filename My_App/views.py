from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import *
from My_App.models import Admin, Course, Staff, Student, Subject
from rest_framework.decorators import api_view
from My_App import serializers
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,DjangoModelPermissions
# Create your views here.

class add_student(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]
    
class add_student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]    

class add_staff(generics.ListCreateAPIView):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_staff_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_admin(generics.ListCreateAPIView):
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_admin_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_course(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]
class add_course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_subject(generics.ListCreateAPIView):
    queryset=Subject.objects.all()
    serializer_class=AdminSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class add_subject_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class student_leave_report(generics.ListCreateAPIView):
    queryset=LeaveReportStudent.objects.all()
    serializer_class=LeaveReportStudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class student_leave_report_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=LeaveReportStudent.objects.all()
    serializer_class=LeaveReportStudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_leave_report(generics.ListCreateAPIView):
    queryset=LeaveReportStaff.objects.all()
    serializer_class=LeaveReportStaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_leave_report_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=LeaveReportStaff.objects.all()
    serializer_class=LeaveReportStaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class student_feedback(generics.ListCreateAPIView):
    queryset=StudentFeedback.objects.all()
    serializer_class=StudentFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class student_feedback_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=StudentFeedback.objects.all()
    serializer_class=StudentFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_feedback(generics.ListCreateAPIView):
    queryset=StaffFeedback.objects.all()
    serializer_class=StaffFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_feedback_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=StaffFeedback.objects.all()
    serializer_class=StaffFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_notification(generics.ListCreateAPIView):
    queryset=StaffNotification.objects.all()
    serializer_class=StaffNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class staff_notification_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=StaffNotification.objects.all()
    serializer_class=StaffNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class admin_notification(generics.ListCreateAPIView):
    queryset=AdminNotification.objects.all()
    serializer_class=AdminNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class admin_notification_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=AdminNotification.objects.all()
    serializer_class=AdminNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]


