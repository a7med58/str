# Generated by Django 4.0.5 on 2022-06-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_remove_book_total_price_book_total_retal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, choices=[('أقتصاد', 'eco'), ('أنتاج حيوانى', 'anp'), ('ألبان', 'alban'), ('حشرات', 'hasharat'), ('حيوان زراعى', 'anagr'), ('فاكهة', 'vig'), ('خضر', 'vig2'), ('زينة', 'zena'), ('أراضى', 'arady'), ('كيمياء حيوية', 'cimical')], default='avalilable', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('avalilable', 'جارى المناقشة'), ('rental', 'تم المناقشة')], default='avalilable', max_length=50, null=True),
        ),
    ]
