from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Invoices(models.Model):
    invoice_number = models.CharField(max_length=200, validators=[alphanumeric])
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=50)
    project_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
