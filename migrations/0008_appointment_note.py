# Generated by Django 4.0.4 on 2022-07-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthpostapp', '0007_bed_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='note',
            field=models.TextField(default='Hope you are having a nice day doctor\nThis is for my general monthly checkup'),
        ),
    ]