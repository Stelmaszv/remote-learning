from django.contrib import admin
from .models import Classroom,Subject,Lesson,Tasks,Dashbord,DashbordType
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Dashbord)
admin.site.register(DashbordType)
admin.site.register(Tasks)
