# Generated by Django 2.2.1 on 2019-12-10 08:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191210_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 8, 24, 5, 99397, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 8, 24, 5, 99397, tzinfo=utc)),
        ),
    ]
