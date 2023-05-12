from django.shortcuts import render,redirect
from bankapp.models import Bank
from bankapp.forms import BankForm, SignUpForm
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
def index(request):
	return render(request,'apps/index.html')
def home(request):
	return render(request,'apps/home.html')
def index1(request):
	return render(request,'apps/index1.html')
def contact(request):
	return render(request,'apps/contact.html')
@login_required
def service(request):
	return render(request,'apps/service.html')
@login_required
def loan(request):
	return render(request,'apps/loan.html')
@login_required
def show(request):
	bank = Bank.objects.all()
	return render(request,'apps/result.html',{'b':bank})
@login_required
def insert(request):
	form = BankForm()
	if request.method=="POST":
		form = BankForm(request.POST)
		if form.is_valid():
			form.save()
		return show(request)
	return render(request,'apps/form.html',{'form':form})
@login_required
def update(request,id):
	bank = Bank.objects.get(id=id)
	if request.method=="POST":
		form=BankForm(request.POST, instance=bank)
		if form.is_valid():
			form.save()
		return redirect('/show')
	return render(request,'apps/update.html',{'b':bank})
@login_required
def delete(request,id):
	bank = Bank.objects.get(id=id)
	bank.delete()
	return redirect('/show')
@login_required
def store(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition']="attachment;filename=customer_details.csv"
	writer=csv.writer(response)
	writer.writerow(['ACC NO','Name','Mobile','City','Deposit','Balance'])
	bank = Bank.objects.all()
	for i in bank:
		writer.writerow([i.account_no,i.name,i.mobile,i.city,i.deposit_amt,i.balance_amt])
	return response
def logout(request):
	return render(request,'apps/logout.html')
def signup_views(request):
	form = SignUpForm()
	if request.method=="POST":
		form = SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'apps/signup.html',{'form':form})
