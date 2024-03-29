# Generated by Django 4.1.2 on 2023-01-01 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_queryresponse_id_map_alter_queryresponse_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('query', models.TextField(null=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
