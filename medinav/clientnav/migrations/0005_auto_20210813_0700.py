# Generated by Django 3.2.3 on 2021-08-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientnav', '0004_ingrediantlist_concentration'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediantlist',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ingrediantlist',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
