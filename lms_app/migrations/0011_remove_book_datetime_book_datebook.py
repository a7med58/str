# Generated by Django 4.0.5 on 2022-06-30 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0010_alter_book_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='datetime',
        ),
        migrations.AddField(
            model_name='book',
            name='datebook',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]