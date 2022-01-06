from django.core.mail import message
from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
from django.core.validators import MinValueValidator

from .models import Invoices


class Invoice_Serializer(serializers.ModelSerializer):
    client_email = serializers.EmailField(required=True,max_length=50,validators=[UniqueValidator(queryset=Invoices.objects.all(),message="A client with this email already exists and the payment link has been sent.")])
    amount = serializers.DecimalField(max_digits=10, decimal_places=3,validators=[MinValueValidator(100,message="Amount should be greater than or equal to 100 (stripe has some min amount)")] )
    client_name = serializers.CharField(max_length=50)

    class Meta:
        model = Invoices
        fields = "__all__"