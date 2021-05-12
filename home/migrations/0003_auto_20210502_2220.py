# Generated by Django 3.0.7 on 2021-05-02 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]