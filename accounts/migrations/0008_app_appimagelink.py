# Generated by Django 3.2.14 on 2023-01-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_completedtask_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='Appimagelink',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
