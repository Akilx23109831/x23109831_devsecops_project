# Generated by Django 4.2.6 on 2023-12-06 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='emp_id',
            new_name='emp_age',
        ),
    ]