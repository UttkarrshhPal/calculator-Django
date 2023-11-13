from django import forms  
class CalculatorForm(forms.Form):
    num1 = forms.IntegerField(label="Enter num1")
    num2 = forms.IntegerField(label="Enter num2")
    opr  = forms.CharField(label="Enter operand",max_length=20)
