# Generated by Django 3.1.8 on 2021-04-08 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BauDB', '0007_delete_today_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='today_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todayDesc', models.CharField(max_length=25)),
                ('keyModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BauDB.key_model')),
            ],
        ),
    ]
