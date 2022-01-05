# Generated by Django 4.0.1 on 2022-01-05 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('client_name', models.CharField(max_length=20)),
                ('client_email', models.EmailField(max_length=20)),
                ('project_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
