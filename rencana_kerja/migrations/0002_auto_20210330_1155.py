# Generated by Django 3.1.5 on 2021-03-30 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rencana_kerja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buatrencana',
            name='user',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
