from rest_framework import serializers
from .models import (Logs, 
                     EmployeeData,
                     AttendanceRecord,)


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = '__all__'


class EmployeeDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeData
        fields = '__all__'


class AttendanceRecordSerializer(serializers.ModelSerializer):
    autocomplete_label = serializers.SerializerMethodField()

    def get_autocomplete_label(self, obj):
        return f"{obj.employee_name} - {obj.employeeid}"
    
    class Meta:
        model = AttendanceRecord
        fields = '__all__'