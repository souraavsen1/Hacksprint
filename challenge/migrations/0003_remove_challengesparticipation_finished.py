# Generated by Django 3.0.7 on 2020-10-03 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20200929_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengesparticipation',
            name='finished',
        ),
    ]