# Generated by Django 3.1.2 on 2020-10-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address'),
        ),
    ]