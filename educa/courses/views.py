from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def home(request):
    courses = MyCourse.objects.all()
    context = {'courses':courses}
    return render(request, 'courses/index.html',context)


def course_listing(request):
    courses = MyCourse.objects.all()
    context = {'courses':courses}
    return render(request, 'courses/courses_listing.html',context)

def course(request,id):
    course = get_object_or_404(MyCourse, id=id)
    available_courses = MyCourse.objects.all().exclude(id=id)
    instructors = Instructor.objects.all()
    context = {'course':course,'instructors':instructors,'available_courses':available_courses}
    return render(request, 'courses/course.html',context)

def about(request):
    instructors = Instructor.objects.all()
    context = {'instructors':instructors}
    return render(request, 'courses/about.html',context)


