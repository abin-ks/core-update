# Generated by Django 4.0.3 on 2022-05-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0016_delete_project_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='acntspayslip',
            name='net_salary',
            field=models.IntegerField(default=0),
        ),
    ]
