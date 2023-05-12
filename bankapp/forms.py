from django import forms
from bankapp.models import Bank
from django.contrib.auth.models import User
class BankForm(forms.ModelForm):
	class Meta:
		model = Bank
		fields = "__all__"
class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']