# Generated by Django 3.1.8 on 2021-04-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='key_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyName', models.CharField(max_length=25)),
                ('keyDesc', models.CharField(max_length=25)),
            ],
        ),
    ]