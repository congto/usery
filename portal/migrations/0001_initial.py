# Generated by Django 2.1 on 2018-08-28 17:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SandbStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('sandb_static', tinymce.models.HTMLField(verbose_name='sandb_static')),
            ],
        ),
    ]