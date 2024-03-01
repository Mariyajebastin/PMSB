from django.db import models


# Create your models here.


class login(models.Model):
	email_id = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "login"
	
	def __str__(self):
		return self.email_id


class manager(models.Model):
	employee_name = models.CharField(max_length=50)
	designation = models.CharField(max_length=100)
	email_id = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	profile_picture = models.ImageField(blank=False)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "manager"
	
	def __str__(self):
		return self.employee_name


class Employee(models.Model):
	employee_name = models.CharField(max_length=50)
	designation = models.CharField(max_length=100)
	email_id = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	dob = models.CharField(max_length=20)
	doj = models.CharField(max_length=20)
	# don't specify any separate folder in to upload the image just leave as it is
	profile_picture = models.ImageField( blank=False)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "employee"
	
	def __str__(self):
		return self.employee_name

# apply migration commands and check again
class Task(models.Model):
	task_name = models.CharField(max_length=100)
	task_brief = models.CharField(max_length=5000)
	date = models.CharField(max_length=20)
	priority = models.CharField(max_length=20)
	attach_file = models.ImageField()
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "tasks"
	
	def __str__(self):
		return self.task_brief


class announcement(models.Model):
	announcement = models.CharField(max_length=5000)
	name = models.CharField(max_length=50)
	date = models.CharField(max_length=20)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = 'announcement'
		
	def __str__(self):
		return self.announcement
