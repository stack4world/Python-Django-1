# Generated by Django 2.0.7 on 2018-09-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockprediction',
            name='accuracy_prev_day',
            field=models.FloatField(blank=True),
        ),
    ]