# Generated by Django 4.2.1 on 2023-10-24 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisdomacademy', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'course')},
        ),
    ]