# Generated by Django 3.0.6 on 2020-05-28 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_auto_20200525_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('starts_at',)},
        ),
    ]