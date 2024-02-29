from rest_framework import serializers

from employee.models import employeeLogin


class EmployeeLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = employeeLogin
		exclude = ["created_time", "created_date"]