# Generated by Django 4.0 on 2021-12-22 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_end_schedule_closetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='Street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='store.street'),
        ),
    ]
