from django.contrib import admin
from django.urls import path 
from apps.admissions import views as admissions_views

urlpatterns = [
    path('addadmission/',admissions_views.add_admission),
    path('addacademicyear/',admissions_views.add_academic_year), 
    path('', admissions_views.homepage, name='home'),

]
