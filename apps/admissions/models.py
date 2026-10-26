from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    CLASS_CHOICES = [
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
    ]    

    admission_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # Fixed max_length and choices syntax
    class_name = models.IntegerField(choices=CLASS_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
 # Fixed missing parentheses
    contact = models.CharField(max_length=15)
    address = models.TextField()
    admission_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class AcademicYear(models.Model):
    year_name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    

