# Generated by Django 4.0.4 on 2022-07-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpostapp', '0005_user_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.TextField()),
                ('img', models.TextField()),
                ('name', models.TextField()),
                ('available', models.IntegerField()),
                ('phone', models.TextField()),
            ],
        ),
    ]