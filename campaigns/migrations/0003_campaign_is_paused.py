# Generated by Django 5.0.2 on 2024-02-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='is_paused',
            field=models.BooleanField(default=False),
        ),
    ]
