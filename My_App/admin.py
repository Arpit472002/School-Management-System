from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(HOD)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(StaffNotification)
admin.site.register(HODNotification)
admin.site.register(StudentFeedback)
admin.site.register(StaffFeedback)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(MyUser)