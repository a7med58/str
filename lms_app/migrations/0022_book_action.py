# Generated by Django 4.0.5 on 2022-07-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0021_remove_book_action_remove_book_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='action',
            field=models.BooleanField(default=True),
        ),
    ]
