from rest_framework import serializers

from main.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Worker
        fields = ['name', 'major', 'salary', 'boss', 'date_work']