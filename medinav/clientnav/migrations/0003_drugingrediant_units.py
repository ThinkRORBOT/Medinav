# Generated by Django 3.2.3 on 2021-05-27 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientnav', '0002_ingrediantlist_i_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugingrediant',
            name='units',
            field=models.CharField(default='g', max_length=50),
        ),
    ]
