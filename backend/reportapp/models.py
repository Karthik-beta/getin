from django.db import models




class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    employeeid = models.IntegerField(blank=True, null=True)
    logdate = models.DateField(blank=True, null=True)
    logtime = models.TimeField(blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    serialno = models.CharField(max_length=100, blank=True, null=True)

class EmployeeData(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(unique=True)
    device_enroll_id = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True, null=True)
    status = models.CharField(max_length=100)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_leaving = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100)



class AttendanceRecord(models.Model):
    employeeid = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    device_enroll_id = models.CharField(max_length=100)
    logdate = models.DateField()
    first_logtime = models.TimeField(blank=True, null=True)
    last_logtime = models.TimeField(blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100)
    shortname = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_time = models.TimeField(blank=True, null=True)
    late_entry = models.TimeField(blank=True, null=True)
    early_exit = models.TimeField(blank=True, null=True)
    overtime = models.TimeField(blank=True, null=True)
    shift_status = models.CharField(max_length=50, blank=True, null=True)
    shift = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    category = models.CharField(max_length=100,blank=True, null=True)
    status = models.CharField(max_length=100)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_leaving = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('employeeid', 'logdate')


from . import signals