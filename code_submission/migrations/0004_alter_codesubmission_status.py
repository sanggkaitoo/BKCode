# Generated by Django 4.0 on 2022-02-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_submission', '0003_alter_codesubmission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesubmission',
            name='status',
            field=models.CharField(choices=[('AC', 'Accepted'), ('WA', 'Wrong Answer'), ('CE', 'Compile Error'), ('TLE', 'Time Limit Exceeded'), ('MLE', 'Memory Limit Exceeded'), ('RE', 'Runtime Error'), ('SE', 'System Error')], max_length=40),
        ),
    ]