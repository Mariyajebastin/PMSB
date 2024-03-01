import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from manager.models import login, manager, Employee, Task, announcement
from manager.serializer import LoginSerializer, ManagerSerializer, EmployeeSerializer, TaskSerializer, \
	AnnouncementSerializer, TaskUpdateSerializer, TaskDeleteSerializer


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
		employees = Employee.objects.all()
		employee_details = EmployeeSerializer(employees, many=True)
		return Response({
			"message": employee_details.data
		})


@api_view(["POST", "GET", "PUT","DELETE"])
def createTask(request, u_id=None):
	response_details = {
		"status": False,
		"status_code": 404,
		"message": "Error happened while processing"
	}
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
		tasks = Task.objects.all()
		task_details = TaskSerializer(tasks, many=True)
		return Response({
			"message": task_details.data
		})

	if request.method == "PUT":
		received_data = TaskUpdateSerializer(data=request.data)
		print("from 97 ",request.data.get("id"))
		# you are not passing value for id key from postman
		# open table of task
		# there is no database name db.sqlite3x
		print("from 106 ",request.data)
		if received_data.is_valid():
			if Task.objects.filter(id=request.data.get("id")).exists():
				tasks = Task.objects.get(id=request.data.get("id"))
				tasks.task_name = received_data.validated_data.get('task_name')
				tasks.task_brief = received_data.validated_data.get('task_brief')
				tasks.date = received_data.validated_data.get('date')
				tasks.priority = received_data.validated_data.get('priority')
				# tasks.attach_file = received_data.validated_data.get('attach_file')
				tasks.save()
				# now start to test i'll check
				response_details.update({
					"status":True,
					"status_code":200,
					"message":"Data updated successfully !"
				})
			else:
				response_details.update({
					"message":"Id is not exists !"
				})
		else:
			return JsonResponse({
				"message": received_data.errors
			})
		
	if request.method == "DELETE":
		if u_id:
			received_data = TaskDeleteSerializer(data={"id": u_id})
			if received_data.is_valid():
				Task.objects.filter(pk=received_data.validated_data.get('id')).delete()
				return JsonResponse({
					"message": "Data deleted successfully"
				})
			else:
				return JsonResponse({
					"message": "There is no Data"
				})
			
	return Response(response_details)


	
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