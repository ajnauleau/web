# Generated by Django 2.0.5 on 2018-05-25 21:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0024_auto_20180523_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsubscriber',
            name='form_submission_records',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[]),
        ),
    ]
