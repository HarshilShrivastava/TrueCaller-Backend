# Generated by Django 3.1.2 on 2020-10-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201009_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Is_User',
            field=models.BooleanField(default=True),
        ),
    ]
