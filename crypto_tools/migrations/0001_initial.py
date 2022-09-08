# Generated by Django 4.1.1 on 2022-09-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(default=1)),
                ('name', models.CharField(default='', max_length=150)),
                ('symbol', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField(db_index=True)),
                ('high', models.FloatField(default=0)),
                ('low', models.FloatField(default=0)),
                ('open', models.FloatField(default=0)),
                ('close', models.FloatField(default=0)),
                ('volume', models.FloatField(default=0)),
                ('market_cap', models.FloatField(default=0)),
            ],
        ),
    ]
