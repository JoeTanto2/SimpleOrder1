# Generated by Django 3.2.7 on 2021-09-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_alter_ourprescriptions_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickedUpPrescriptions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('medicine', models.CharField(max_length=100)),
                ('patinet_name', models.CharField(max_length=100)),
                ('doctor_id', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
