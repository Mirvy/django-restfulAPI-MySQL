from rest_framework import serializers
from tasks.models import Task, Client

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','description','body','urgent','created','updated','due','client')

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id','name','description','scope','email','notes','created','updated')