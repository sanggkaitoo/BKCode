# Generated by Django 4.0 on 2022-01-14 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_categoryexercise_alter_exercise_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='exercise.categoryexercise'),
            preserve_default=False,
        ),
    ]