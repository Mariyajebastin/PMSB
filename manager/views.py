import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from manager.models import login, manager, employee, task, announcement
from manager.serializer import LoginSerializer, ManagerSerializer, EmployeeSerializer, TaskSerializer, \
	AnnouncementSerializer


# Create your views here.


@api_view(["POST", "GET"])
def managerLogin(request):
	if request.method == "POST":
		request_data = LoginSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	
	if request.method == "GET":
		logins = login.objects.all()
		login_details = LoginSerializer(logins, many=True)
		return Response({
			"message": login_details.data
		})
		
		
@api_view(["POST", "GET"])
def createManager(request):
	if request.method == "POST":
		request_data = ManagerSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	if request.method == "GET":
		managers = manager.objects.all()
		manager_details = ManagerSerializer(managers, many=True)
		return Response({
			"message": manager_details.data
		})


@api_view(["POST", "GET"])
def createEmployee(request):
	if request.method == "POST":
		request_data = EmployeeSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	if request.method == "GET":
		employees = employee.objects.all()
		employee_details = EmployeeSerializer(employees, many=True)
		return Response({
			"message": employee_details.data
		})


@api_view(["POST", "GET"])
def createTask(request):
	if request.method == "POST":
		request_data = TaskSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	if request.method == "GET":
		tasks = task.objects.all()
		task_details = TaskSerializer(tasks, many=True)
		return Response({
			"message": task_details.data
		})


@api_view(["POST", "GET"])
def createAnnouncement (request):
	if request.method == "POST":
		request_data = AnnouncementSerializer(data=request.data)
		if request_data.is_valid():
			request_data.save()
			return JsonResponse({
				"message": "Data saved successfully"
			})
		else:
			return Response(request_data.errors)
	
	if request.method == "GET":
		announcements = announcement.objects.all()
		announcement_details = AnnouncementSerializer(announcements, many=True)
		return Response({
			"message": announcement_details.data
		})