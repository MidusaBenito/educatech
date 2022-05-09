from django.contrib import admin

from .models import *

@admin.register(MyCourse)
class MyCourseAdmin(admin.ModelAdmin):
    #def first_name(self,user):
        #return user.user.first_name

    #def last_name(self,user):
        #return user.user.last_name

    list_display = ["course_name"]
    list_filter = ["course_name"]

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    #def first_name(self,user):
        #return user.user.first_name

    #def last_name(self,user):
        #return user.user.last_name

    list_display = ["instructor_name","course_teaching"]
    list_filter = ["instructor_name","course_teaching"]
