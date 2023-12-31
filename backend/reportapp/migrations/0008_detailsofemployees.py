# Generated by Django 4.2.4 on 2023-08-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0007_processedgislogs_delete_employeelogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='detailsOfEmployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('device_enroll_id', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
            ],
        ),
    ]
