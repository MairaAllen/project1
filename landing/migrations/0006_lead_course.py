# Generated by Django 4.1.7 on 2023-04-10 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_lead_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landing.course'),
            preserve_default=False,
        ),
    ]
