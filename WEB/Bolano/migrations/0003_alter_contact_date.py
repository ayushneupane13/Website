# Generated by Django 4.0.4 on 2022-06-02 04:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bolano', '0002_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 2, 4, 46, 45, 665451, tzinfo=utc)),
            preserve_default=False,
        ),
    ]