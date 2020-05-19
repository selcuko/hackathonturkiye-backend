# Generated by Django 3.0.6 on 2020-05-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20200518_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='prize',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
