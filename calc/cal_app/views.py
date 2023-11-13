from django.shortcuts import render
from .forms import CalculatorForm
def view1(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            opr  = form.cleaned_data['opr']

            if opr == '+':
                result = num1+num2
            elif opr == '-':
                result = num1-num2
            elif opr == '*':
                result = num1*num2
            elif opr == '/':
                if num2!=0:
                  result = num1/num2 
                else:
                    result = 'Cannot divide by Zero'
    else:
        form = CalculatorForm()
    return render(request,'Templates/index.html',{'form':form,'result':result})                






