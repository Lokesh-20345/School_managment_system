from django.db import models
from apps.admissions.models import AcademicYear, Student
# Create your models here.
class FeeStructure(models.Model):
    academic_year = models.ForeignKey(
        AcademicYear, on_delete=models.CASCADE
    )
    classname = models.DecimalField(max_digits=10, decimal_places=2)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['academic_year','classname'],
            name = 'Unique_fee_structure_academic_year_classname',
        )
    ]
    
class StudentFeeAccount(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    fee_paid =models.DecimalField(max_digits=10, decimal_places=2)
    fee_due =models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=['student','academic_year'],
                    name = 'Unique_feeAccount_student_academic_year',
                )
            ]
    
class FeePayment(models.Model):
    payment_mode = [
        ('UPI','UPI'),
        ('CASH','CASH'),
        ('Card','Card'),
        ('Bank','Bank')    
    ]
    Student_fee_account = models.ForeignKey(StudentFeeAccount,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    mode = models.CharField(max_length=10,choices=payment_mode)
    remark = models.CharField(max_length=100)
    
    