# Generated by Django 4.1.2 on 2022-12-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_site', '0004_extrasorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrasorder',
            name='username',
        ),
        migrations.AddField(
            model_name='extrasorder',
            name='item_name',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='extrasorder',
            name='item_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='extrasorder',
            name='meal_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]