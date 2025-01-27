# Generated by Django 4.2.6 on 2023-11-14 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0001_initial'),
        ('property_app', '0005_alter_property_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_owner', to='signup_login_app.user'),
        ),
    ]
