# Generated by Django 4.1.3 on 2022-11-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_employee_employees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departaments',
            new_name='Departments',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='departament_name',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='departament_name',
            new_name='department_name',
        ),
    ]
