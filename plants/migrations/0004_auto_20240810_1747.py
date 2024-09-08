# Generated by Django 3.1.14 on 2024-08-10 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_plant_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='post_date',
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]