# Generated by Django 4.2.1 on 2023-10-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_student_notification_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_notification',
            name='message',
            field=models.TextField(default=3333),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_feedback',
            name='feedback',
            field=models.TextField(max_length=500),
        ),
    ]