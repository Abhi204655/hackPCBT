# Generated by Django 2.2.6 on 2020-02-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='addres',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='land',
            name='inv',
        ),
        migrations.RemoveField(
            model_name='land',
            name='sell',
        ),
    ]
