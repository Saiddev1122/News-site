# Generated by Django 3.2.8 on 2021-10-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='toliq_malumot',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
