# Generated by Django 4.0.1 on 2022-11-11 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_business_location_lat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_owner',
            new_name='owner',
        ),
    ]
