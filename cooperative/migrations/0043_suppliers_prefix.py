# Generated by Django 3.2.8 on 2022-01-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0042_purchase_header_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliers',
            name='prefix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
