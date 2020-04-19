# Generated by Django 3.0.5 on 2020-04-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('panno', models.CharField(max_length=30)),
                ('about', models.TextField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=10)),
                ('averageRating', models.FloatField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
