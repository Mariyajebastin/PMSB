from rest_framework import serializers

from manager.models import login, manager, employee, task, announcement


class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = login
		exclude = ["created_time", "created_date"]


class ManagerSerializer(serializers.ModelSerializer):
	class Meta:
		model = manager
		exclude = ["created_time", "created_date"]
		
		
class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = employee
		exclude = ["created_time", "created_date"]


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = task
		exclude = ["created_time", "created_date"]
		
		
class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = announcement
		exclude = ["created_time", "created_date"]