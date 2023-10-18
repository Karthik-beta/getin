# Generated by Django 4.2.4 on 2023-08-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employeeDetails',
            fields=[
                ('EMPLOYEE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('DEVICE_ENROLL_ID', models.CharField(max_length=100)),
                ('EMPLOYEE_NAME', models.CharField(max_length=100)),
                ('COMPANY', models.CharField(max_length=100)),
                ('LOCATION', models.CharField(max_length=100)),
                ('JOB_TYPE', models.CharField(max_length=100)),
                ('DEPARTMENT', models.CharField(max_length=100)),
                ('DESIGNATION', models.CharField(max_length=100)),
                ('CATEGORY', models.CharField(max_length=100)),
                ('STATUS', models.CharField(max_length=100)),
                ('DATE_OF_JOINING', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='employeeLogs',
            fields=[
                ('EMPLOYEE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('DIRECTION', models.CharField(max_length=100)),
                ('SHORTNAME', models.CharField(max_length=100)),
                ('SERIALNO', models.CharField(max_length=100)),
                ('LOGDATE', models.DateField()),
                ('FIRST_LOGTIME', models.TimeField()),
                ('LAST_LOGTIME', models.TimeField()),
                ('TOTAL_LOGTIME', models.DurationField()),
            ],
        ),
        migrations.DeleteModel(
            name='ProcessedData',
        ),
        migrations.DeleteModel(
            name='RawData',
        ),
    ]
