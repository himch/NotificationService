# Generated by Django 5.0.2 on 2024-02-08 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_options'),
        ('clients', '0001_initial'),
        ('sms', '0006_historicalsms_file_sms_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smsddd', to='campaigns.campaign'),
        ),
        migrations.AlterField(
            model_name='sms',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smsdddd', to='clients.client'),
        ),
    ]
