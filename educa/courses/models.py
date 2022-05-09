from django.db import models
from django.urls import reverse 

class MyCourse(models.Model):
    course_name = models.CharField(max_length=50,default="",null=True)
    course_desc = models.CharField(max_length=300,default="",null=True)
    

    def get_absolute_url(self):
        return reverse('course',
            args=[self.id])

class Instructor(models.Model):
    instructor_name = models.CharField(max_length=50,default="",null=True)
    course_teaching = models.CharField(max_length=50,default="",null=True)
