# Generated by Django 4.2.6 on 2023-11-20 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0007_rename_owner_id_property_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='agent_id',
        ),
        migrations.RemoveField(
            model_name='property',
            name='support_id',
        ),
        migrations.RemoveField(
            model_name='property',
            name='user_id',
        ),
    ]
