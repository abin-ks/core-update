# Generated by Django 4.0.3 on 2022-04-22 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0005_probation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='probation',
            options={'get_latest_by': ['status']},
        ),
    ]
