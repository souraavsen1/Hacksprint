# Generated by Django 3.0.7 on 2020-07-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_track_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
