# Generated by Django 4.2.6 on 2023-11-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0004_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(default='stock.jpg', max_length=50, null=True),
        ),
    ]
