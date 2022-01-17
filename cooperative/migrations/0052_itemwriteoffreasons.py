# Generated by Django 3.2.8 on 2022-01-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0051_alter_stock_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemWriteOffReasons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'itemwriteoffreasons',
                'ordering': ['title'],
                'abstract': False,
            },
        ),
    ]
