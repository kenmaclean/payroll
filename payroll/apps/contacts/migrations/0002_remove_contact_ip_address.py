# Generated by Django 3.1.6 on 2021-02-19 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='ip_address',
        ),
    ]