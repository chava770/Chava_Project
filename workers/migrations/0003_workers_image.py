# Generated by Django 4.1.7 on 2023-03-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_rename_manager_workers_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='IMAGE',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]