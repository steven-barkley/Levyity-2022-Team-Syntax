# Generated by Django 4.1.2 on 2022-10-09 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parkreservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('parkname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('pavillion', models.PositiveIntegerField()),
            ],
        ),
    ]