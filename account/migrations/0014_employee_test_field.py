# Generated by Django 5.0.4 on 2024-05-08 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_employee_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='test_field',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Accountant'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
