# Generated by Django 2.2.4 on 2019-08-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0002_auto_20190808_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='location',
        ),
        migrations.AddField(
            model_name='screen',
            name='location',
            field=models.ManyToManyField(to='screens.Location'),
        ),
    ]
