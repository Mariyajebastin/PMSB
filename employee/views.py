from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.serializer import EmployeeLoginSerializer


# Create your views here.

@api_view(["POST", "GET"])
def employeeLogin(request):
	if request.method == "POST":
		request_data = EmployeeLoginSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	if request.method == "GET":
		employees = employeeLogin.objects.all()
		employee_details = EmployeeLoginSerializer(employees, many=True)
		return Response({
			"message": employee_details.data
		})