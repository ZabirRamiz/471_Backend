# Generated by Django 4.2.6 on 2023-11-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0003_session_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
