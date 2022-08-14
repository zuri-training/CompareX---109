# Generated by Django 4.1 on 2022-08-13 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='uploads/')),
                ('operation', models.CharField(choices=[('conversion', 'Conversion'), ('highlight_duplicates_single', 'Highlight Duplicates Single'), ('remove_duplicates_single', 'Remove Duplicates Single'), ('highlight_duplicates_double', 'Highlight Duplicates Double'), ('remove_duplicates_double', 'Remove Duplicates Double')], max_length=30)),
                ('date_performed', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]