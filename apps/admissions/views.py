from django.shortcuts import render
from apps.admissions.forms import StudentModelForm, AcademicYearForm
from apps.admissions.models import AcademicYear
from apps.finance.models import FeeStructure, StudentFeeAccount
# Create your views here.
def homepage(request):
    return render(request,'home.html')


def add_academic_year(request):
    form = AcademicYearForm
    my_form = {'form': form}
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
    return render(request, 'admissions/add_academic_year.html', my_form)

def add_admission(request):
    form = StudentModelForm()
    my_form =  {'form':form}
    if request.method == 'POST':
        filled_form = StudentModelForm(request.POST)
        student = filled_form.save()
        current_academic_year = AcademicYear.objects.get(is_active =True)
        fee_structures = FeeStructure.objects.filter(academic_year = current_academic_year) & FeeStructure.objects.filter( classname = student.name)
        total_fee = fee_structures[0].total_fee
        
        student_fee_accout = StudentFeeAccount.objects.create(student = student,academic_year = current_academic_year,total_fee = total_fee,fee_paid = 0, fee_due = total_fee)
    return render(request,'admissions/add_admission.html',my_form)

def admission_report(request):
    pass

def update_student(request):
    pass
 
def delete_student(request):
    pass
