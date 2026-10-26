from django import forms 
from apps.admissions.models import Student, AcademicYear


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'admission_number','name','father_name','mother_name',
            'gender','class_name','date_of_birth','contact','address'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
            'gender' : forms.RadioSelect,
            'class_name' : forms.Select,
        }
        
class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = [
            'year_name','is_active'
        ]
            
    