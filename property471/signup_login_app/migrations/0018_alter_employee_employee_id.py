# Generated by Django 4.2.6 on 2023-12-06 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login_app', '0017_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee_id', serialize=False, to='signup_login_app.user'),
        ),
    ]
