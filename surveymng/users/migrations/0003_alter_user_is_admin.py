# Generated by Django 3.2.15 on 2022-09-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
