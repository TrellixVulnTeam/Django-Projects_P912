# Generated by Django 3.1.4 on 2020-12-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email1',
            field=models.CharField(default='SOME Eamil', max_length=140),
        ),
        migrations.AddField(
            model_name='employee',
            name='name1',
            field=models.CharField(default='SOME Name', max_length=140),
        ),
    ]