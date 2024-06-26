# Generated by Django 4.0 on 2022-03-14 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('exercise', '0011_alter_exercise_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='auth.user'),
        ),
    ]
