# Generated by Django 4.2.6 on 2023-11-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='agent_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='support_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
