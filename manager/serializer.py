from rest_framework import serializers

from manager.models import login, manager, Employee, Task, announcement


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
		model = Employee
		exclude = ["created_time", "created_date"]


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		exclude = ["created_time", "created_date"]
	
		

class TaskUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		exclude = ["created_time", "created_date","attach_file"]
	
	
class TaskDeleteSerializer(serializers.Serializer):
	id = serializers.CharField(max_length=10)

class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = announcement
		exclude = ["created_time", "created_date"]