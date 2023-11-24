# Generated by Django 4.2.6 on 2023-11-20 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0002_remove_session_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='user_id',
            field=models.ForeignKey(default='user_1', on_delete=django.db.models.deletion.CASCADE, to='signup_login_app.user'),
            preserve_default=False,
        ),
    ]
