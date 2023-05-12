from django.db import models
class Bank(models.Model):
	account_no = models.IntegerField()
	name = models.CharField(max_length=64)
	mobile = models.IntegerField()
	city = models.CharField(max_length=64)
	deposit_amt = models.IntegerField()
	balance_amt = models.IntegerField()
