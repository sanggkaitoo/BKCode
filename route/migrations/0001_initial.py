# Generated by Django 4.0 on 2022-03-19 01:49

from django.db import migrations, models
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', django_editorjs_fields.fields.EditorJsTextField()),
            ],
        ),
    ]
