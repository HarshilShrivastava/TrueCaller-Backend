# Generated by Django 3.1.2 on 2020-10-09 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone_number', phone_field.models.PhoneField(max_length=31)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Marked_Spam_no', models.PositiveIntegerField(default=0)),
                ('Registered_user', models.BooleanField(default=False)),
                ('In_List', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_person_contact_list', to=settings.AUTH_USER_MODEL)),
                ('Marked_by', models.ManyToManyField(blank=True, related_name='marked_by_these_many_peoples', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
