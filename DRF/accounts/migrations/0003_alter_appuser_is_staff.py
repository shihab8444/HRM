# Generated by Django 5.0.4 on 2024-05-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_appuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
