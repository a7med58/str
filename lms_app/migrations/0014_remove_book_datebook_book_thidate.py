# Generated by Django 4.0.5 on 2022-06-30 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0013_rename_date_book_datebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='datebook',
        ),
        migrations.AddField(
            model_name='book',
            name='thidate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
