# Generated by Django 5.1.5 on 2025-02-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.CharField(choices=[('available', 'Available'), ('closed', 'Closed'), ('unavailable', 'Unavailable')], default='available', max_length=20)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
