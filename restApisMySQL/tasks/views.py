from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST','DELETE'])
def task_list(request):
    # GET list of tasks, POST new task, DELETE all tasks
    if request.method == 'GET':
        tasks = Task.objects.all()

        description = request.GET.get('description',None)
        if description is not None:
            tasks = tasks.filter(description__icontains=description)

        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message':f'{count[0]} Tasks were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET','PUT','DELETE'])
def task_detail(request, pk):
    # find task by pk (id)
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({'message': 'The task does not exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data)
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def task_list_urgent(request):
    tasks = Task.objects.filter(urgent=True)

    if request.method == 'GET':
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
