# Generated by Django 2.2.6 on 2020-02-07 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_remove_land_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
