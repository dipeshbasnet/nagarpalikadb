# Generated by Django 4.0.1 on 2022-11-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_business_taxhistory_landlord_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='status',
            field=models.CharField(default='APPROVED', max_length=10),
            preserve_default=False,
        ),
    ]
