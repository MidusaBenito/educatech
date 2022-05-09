from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('course/',views.course_listing, name='course_listing'),
    path('view-course/<int:id>/',views.course, name='course'),
    path('about/',views.about, name='about'),
]