# Generated by Django 3.0.6 on 2020-05-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='role',
            field=models.ForeignKey(blank=True, limit_choices_to=5, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_auth.Role'),
        ),
    ]
