# Generated by Django 4.0 on 2021-12-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_squashed_0004_alter_schedule_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='Comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
