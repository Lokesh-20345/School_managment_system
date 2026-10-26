from django.shortcuts import render
from apps.finance.forms import FeeStructureForm, FeePaymentForm
from apps.admissions.views import homepage

# Create your views here.
def set_fee_structure(request):
    form = FeeStructureForm
    my_form = {'form':form}
    if request.method == 'POST':
        form = FeeStructureForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)
    return render(request,'finance/set_fee_structure.html',my_form)


def collect_fee(request):
    form = FeePaymentForm
    my_form = {'form':form}
    # if request.method == "POST":
    #     form = FeePaymentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    return render(request,"finance/Collect_fee.html",my_form)