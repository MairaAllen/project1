# Generated by Django 4.1.7 on 2023-04-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
