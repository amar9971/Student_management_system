# Generated by Django 4.2.1 on 2023-06-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_staff_notification_staff_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_leave',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff_notification',
            name='message',
            field=models.TextField(),
        ),
    ]
