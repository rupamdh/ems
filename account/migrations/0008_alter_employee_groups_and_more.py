# Generated by Django 5.0.4 on 2024-05-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_employee_options_alter_employee_adhar_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='employee_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, null=True, related_name='employee_user_permissions', to='auth.permission'),
        ),
    ]
