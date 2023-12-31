# Generated by Django 4.2.4 on 2023-08-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0004_alter_employeelogs_direction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gislogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idno', models.IntegerField(blank=True, null=True)),
                ('employeeid', models.IntegerField(blank=True, null=True)),
                ('logdate', models.DateField(blank=True, null=True)),
                ('logtime', models.TimeField(blank=True, null=True)),
                ('direction', models.CharField(blank=True, max_length=50, null=True)),
                ('shortname', models.CharField(blank=True, max_length=50, null=True)),
                ('serialno', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
