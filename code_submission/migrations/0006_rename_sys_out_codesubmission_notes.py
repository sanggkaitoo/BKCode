# Generated by Django 4.0 on 2022-02-26 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('code_submission', '0005_codesubmission_sys_out'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codesubmission',
            old_name='sys_out',
            new_name='notes',
        ),
    ]