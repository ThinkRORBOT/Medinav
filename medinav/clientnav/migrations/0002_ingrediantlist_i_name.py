# Generated by Django 3.2.3 on 2021-05-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientnav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediantlist',
            name='i_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
