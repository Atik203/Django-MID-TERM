# Generated by Django 5.0.3 on 2024-04-09 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_models', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='car_models.carmodel'),
        ),
    ]
