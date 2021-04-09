# Generated by Django 3.1.8 on 2021-04-09 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BauDB', '0009_auto_20210408_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='thisWeek_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thisWeekDesc', models.CharField(max_length=100)),
                ('keyModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BauDB.key_model')),
            ],
        ),
    ]
