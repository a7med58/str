# Generated by Django 4.0.5 on 2022-06-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0017_rename_status_deptn_rename_dept_statusn_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Statusn',
            new_name='Dept',
        ),
        migrations.RenameModel(
            old_name='Deptn',
            new_name='Status',
        ),
        migrations.RemoveField(
            model_name='book',
            name='deptnew',
        ),
        migrations.RemoveField(
            model_name='book',
            name='statusnew',
        ),
    ]
