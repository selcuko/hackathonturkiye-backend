# Generated by Django 3.2.4 on 2021-07-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
