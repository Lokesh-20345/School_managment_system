from django import forms
from apps.finance.models import FeeStructure, FeePayment

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['academic_year','classname','total_fee']
    
class FeePaymentForm(forms.ModelForm):
    class meta:
        model = FeePayment
        fields = ['Student_fee_account','amount','payment_date','payment_mode','remark']