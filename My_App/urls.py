from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentapi',add_student)
router.register('staffapi',add_staff)
router.register('HODapi',add_HOD)
router.register('courseapi',add_course)
router.register('subjectapi',add_subject)
router.register('student_leave_reportapi',student_leave_report)
router.register('staff_leave_reportapi',staff_leave_report)
router.register('student_feedbackapi',student_feedback)
router.register('staff_feedbackapi',staff_feedback)
router.register('staff_notificationapi',staff_notification)
router.register('HOD_notificationapi',HOD_notification)
urlpatterns = [
    path('',include(router.urls))
]
