# Generated by Django 4.1.3 on 2022-11-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_departaments_departments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
