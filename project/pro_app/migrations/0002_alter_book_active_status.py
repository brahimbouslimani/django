# Generated by Django 3.2.9 on 2021-11-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='active_status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('retal', 'retal'), ('sold', 'sold')], max_length=50, null=True),
        ),
    ]
