from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import *
from My_App.models import HOD, Course, Staff, Student, Subject
from rest_framework.decorators import api_view
from My_App import serializers
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from django.core.mail import send_mail
from rest_framework import viewsets
# Create your views here.
@csrf_exempt
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            person_email=request.POST.get('email')
            person_name=request.POST.get('username')
            person_post=request.POST.get('post')
            send_mail('Welcome to our School ','Hey, '+str(person_name)+' From now onwards you are a member of our school at a post of '+str(person_post),'sarpit623@gmail.com',[person_email,],fail_silently=False)
            data['response'] = "successfully registered a new user"
            return Response(data)
        else:
            data = serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

class add_student(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
class add_staff(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

class add_HOD(viewsets.ModelViewSet):
    queryset=HOD.objects.all()
    serializer_class=HODSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class add_course(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class add_subject(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=HODSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class student_leave_report(viewsets.ModelViewSet):
    queryset=LeaveReportStudent.objects.all()
    serializer_class=LeaveReportStudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class staff_leave_report(viewsets.ModelViewSet):
    queryset=LeaveReportStaff.objects.all()
    serializer_class=LeaveReportStaffSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class student_feedback(viewsets.ModelViewSet):
    queryset=StudentFeedback.objects.all()
    serializer_class=StudentFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class staff_feedback(viewsets.ModelViewSet):
    queryset=StaffFeedback.objects.all()
    serializer_class=StaffFeedbackSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class staff_notification(viewsets.ModelViewSet):
    queryset=StaffNotification.objects.all()
    serializer_class=StaffNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]


class HOD_notification(viewsets.ModelViewSet):
    queryset=HODNotification.objects.all()
    serializer_class=HODNotificationSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    


