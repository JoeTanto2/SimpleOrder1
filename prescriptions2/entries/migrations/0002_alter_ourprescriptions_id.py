# Generated by Django 3.2.7 on 2021-09-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourprescriptions',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
