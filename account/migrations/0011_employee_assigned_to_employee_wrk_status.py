# Generated by Django 5.0.4 on 2024-05-08 09:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='wrk_status',
            field=models.CharField(choices=[('WK', 'Working'), ('AV', 'Available'), ('BK', 'Booked'), ('AS', 'Assist'), ('AB', 'Absent')], default='WK', max_length=2, verbose_name='Working Status'),
        ),
    ]
