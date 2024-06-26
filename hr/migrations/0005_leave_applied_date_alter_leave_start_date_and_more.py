# Generated by Django 5.0.4 on 2024-05-13 10:07

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_leave_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='applied_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 13, 10, 7, 43, 143633, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='leave',
            unique_together={('start_date', 'employee')},
        ),
    ]
