# Generated by Django 4.0.1 on 2022-02-05 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.CharField(default='19:52:11', max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.CharField(default=datetime.date(2022, 2, 5), max_length=10),
        ),
    ]