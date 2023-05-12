from django.contrib import admin
from bankapp.models import Bank
class BankAdmin(admin.ModelAdmin):
	list_display = ['account_no','name','mobile','city','deposit_amt','balance_amt']
admin.site.register(Bank,BankAdmin)
