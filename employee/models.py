from django.db import models

# Create your models here.


class employeeLogin(models.Model):
	email_id = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "employer_login"
	
	def __str__(self):
		return self.email_id

