# Generated by Django 4.1.7 on 2023-03-27 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workers',
            old_name='manager',
            new_name='MANAGER',
        ),
    ]
