# Generated by Django 4.2.6 on 2023-11-15 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0006_alter_property_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='owner_id',
            new_name='user_id',
        ),
    ]
