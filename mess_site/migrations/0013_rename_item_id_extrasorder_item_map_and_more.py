# Generated by Django 4.1.2 on 2023-01-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_site', '0012_remove_extrasorder_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrasorder',
            old_name='item_id',
            new_name='item_map',
        ),
        migrations.AddField(
            model_name='extrasorder',
            name='order_month',
            field=models.IntegerField(null=True),
        ),
    ]