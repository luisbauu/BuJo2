# Generated by Django 3.1.8 on 2021-04-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BauDB', '0005_today_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='today_model',
            name='todayDesc',
            field=models.CharField(max_length=25),
        ),
    ]
