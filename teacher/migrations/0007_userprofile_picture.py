# Generated by Django 4.2.1 on 2023-09-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_alter_userprofile_application_letter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='dp/'),
        ),
    ]