# Generated by Django 3.1.8 on 2021-04-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BauDB', '0002_profile_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='profileImage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
