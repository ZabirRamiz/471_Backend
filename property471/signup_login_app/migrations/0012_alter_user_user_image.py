# Generated by Django 4.2.6 on 2023-11-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0011_alter_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
