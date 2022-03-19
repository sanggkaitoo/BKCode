# Generated by Django 4.0 on 2022-03-08 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercise', '0010_exercise_test_input_exercise_test_output'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('organizer', models.CharField(max_length=100)),
                ('date_start', models.DateTimeField()),
                ('data_end', models.DateTimeField()),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ContestDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.exercise')),
            ],
        ),
    ]