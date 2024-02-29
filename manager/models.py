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
	profile_picture = models.ImageField(upload_to="portal_image", blank=False)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "manager"
	
	def __str__(self):
		return self.employee_name


class employee(models.Model):
	employee_name = models.CharField(max_length=50)
	designation = models.CharField(max_length=100)
	email_id = models.CharField(max_length=50)
	password = models.CharField(max_length=10)
	dob = models.CharField(max_length=20)
	doj = models.CharField(max_length=20)
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "employee"
	
	def __str__(self):
		return self.employee_name


class task(models.Model):
	task_brief = models.CharField(max_length=5000)
	date = models.CharField(max_length=20)
	priority = models.CharField(max_length=20)
	attach_file = models.FileField()
	created_time = models.TimeField(auto_now=True)
	created_date = models.DateField(auto_now=True)
	
	class Meta:
		db_table = "task"
	
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
