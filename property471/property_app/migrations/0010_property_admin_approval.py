# Generated by Django 4.2.6 on 2023-11-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0009_property_agent_id_property_support_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='admin_approval',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
