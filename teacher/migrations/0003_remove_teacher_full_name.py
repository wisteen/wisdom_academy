# Generated by Django 4.2.1 on 2023-08-30 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacher_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='full_name',
        ),
    ]