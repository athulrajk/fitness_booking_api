# Generated by Django 5.2.2 on 2025-06-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessclass',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
