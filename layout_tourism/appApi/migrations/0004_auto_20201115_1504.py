# Generated by Django 3.1.3 on 2020-11-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0003_property_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='state_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
