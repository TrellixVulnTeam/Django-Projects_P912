# Generated by Django 3.1.4 on 2020-12-17 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_student_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
    ]