# Generated by Django 3.0.4 on 2020-05-16 04:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0014_auto_20200516_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessanger_detail',
            name='pay_done',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2020, 5, 16, 4, 33, 9, 75053, tzinfo=utc), max_length=19),
        ),
    ]
