# Generated by Django 5.0.2 on 2024-02-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField()),
                ('time_finish', models.DateTimeField()),
                ('text', models.CharField(max_length=160)),
                ('filter', models.CharField(max_length=100)),
            ],
        ),
    ]