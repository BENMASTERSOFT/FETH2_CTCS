# Generated by Django 3.2.8 on 2022-01-13 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0046_auto_20220113_2122'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='accounttypes',
            table='accounttypes',
        ),
        migrations.AlterModelTable(
            name='admincharges',
            table='admincharges',
        ),
        migrations.AlterModelTable(
            name='banks',
            table='banks',
        ),
        migrations.AlterModelTable(
            name='customerid',
            table='customerid',
        ),
        migrations.AlterModelTable(
            name='datacapturemanager',
            table='datacapturemanager',
        ),
        migrations.AlterModelTable(
            name='defaultpassword',
            table='defaultpassword',
        ),
        migrations.AlterModelTable(
            name='departments',
            table='departments',
        ),
        migrations.AlterModelTable(
            name='gender',
            table='gender',
        ),
        migrations.AlterModelTable(
            name='interestdeductionsource',
            table='interestdeductionsource',
        ),
        migrations.AlterModelTable(
            name='loanmergestatus',
            table='loanmergestatus',
        ),
        migrations.AlterModelTable(
            name='loansuploadstatus',
            table='loanuploadstatus',
        ),
        migrations.AlterModelTable(
            name='locations',
            table='locations',
        ),
        migrations.AlterModelTable(
            name='multipleloanstatus',
            table='multipleloanstatus',
        ),
        migrations.AlterModelTable(
            name='nokrelationships',
            table='nokrelationships',
        ),
        migrations.AlterModelTable(
            name='paymentchannels',
            table='paymentchannels',
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='productcategory',
        ),
        migrations.AlterModelTable(
            name='receiptstatus',
            table='receiptstatus',
        ),
        migrations.AlterModelTable(
            name='receipttypes',
            table='receipttypes',
        ),
        migrations.AlterModelTable(
            name='salaryinstitution',
            table='salaryinstitution',
        ),
        migrations.AlterModelTable(
            name='salescategory',
            table='salescategory',
        ),
        migrations.AlterModelTable(
            name='states',
            table='states',
        ),
        migrations.AlterModelTable(
            name='ticketstatus',
            table='ticketstatus',
        ),
        migrations.AlterModelTable(
            name='titles',
            table='titles',
        ),
        migrations.AlterModelTable(
            name='transactionperiods',
            table='transactionperiods',
        ),
        migrations.AlterModelTable(
            name='transactionsources',
            table='transactionsources',
        ),
        migrations.AlterModelTable(
            name='userslevel',
            table='userslevel',
        ),
    ]