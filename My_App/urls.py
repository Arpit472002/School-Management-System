from django.urls import path
from .views import *
urlpatterns = [
    path('add_students/',add_student.as_view()),
    path('add_staffs/',add_staff.as_view()),
    path('add_admins/',add_admin.as_view()),
    path('add_courses/',add_course.as_view()),
    path('add_subjects/',add_subject.as_view()),
    path('student_leave_report/',student_leave_report.as_view()),
    path('staff_leave_report/',staff_leave_report.as_view()),
    path('student_feedback/',student_feedback.as_view()),
    path('staff_feedback/',staff_feedback.as_view()),
    path('admin_notification/',admin_notification.as_view()),
    path('staff_notification/',staff_notification.as_view()),
    path('add_students/<int:pk>/',add_student_detail.as_view()),
    path('add_staffs/<int:pk>/',add_staff_detail.as_view()),
    path('add_admins/<int:pk>/',add_admin_detail.as_view()),
    path('add_courses/<int:pk>/',add_course_detail.as_view()),
    path('add_subjects/<int:pk>/',add_subject_detail.as_view()),
    path('student_leave_report/<int:pk>/',student_leave_report_detail.as_view()),
    path('staff_leave_report/<int:pk>/',staff_leave_report_detail.as_view()),
    path('student_feedback/<int:pk>/',student_feedback_detail.as_view()),
    path('staff_feedback/<int:pk>/',staff_feedback_detail.as_view()),
    path('admin_notification/<int:pk>/',admin_notification_detail.as_view()),
    path('staff_notification/<int:pk>/',staff_notification_detail.as_view())



]
