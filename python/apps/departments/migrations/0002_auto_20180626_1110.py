# Generated by Django 2.0.6 on 2018-06-26 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='requirement',
            old_name='department_id',
            new_name='department',
        ),
    ]