# Generated by Django 4.0.4 on 2022-06-02 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthpostapp', '0002_alter_blood_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='img',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='specialist',
        ),
    ]
