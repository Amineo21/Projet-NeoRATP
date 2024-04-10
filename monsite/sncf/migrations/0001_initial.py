# Generated by Django 5.0.3 on 2024-04-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('trainId', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField()),
                ('destination', models.CharField(max_length=20)),
                ('date', models.TimeField()),
            ],
        ),
    ]
