# Generated by Django 3.1.6 on 2021-02-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name_full_text', models.CharField(max_length=100)),
                ('file_id', models.IntegerField()),
                ('record_date', models.DateTimeField(verbose_name='date of time recorded')),
                ('hours_worked_float', models.FloatField()),
                ('employee_id', models.IntegerField()),
                ('job_group', models.CharField(max_length=1)),
            ],
        ),
    ]
