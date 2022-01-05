from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Invoices


class Invoice_Serializer(serializers.ModelSerializer):
    client_email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=Invoices.objects.all(),message="An client with this email already exists")])
    amount = serializers.DecimalField(max_digits=10, decimal_places=3)
    client_email = serializers.CharField(max_length=50)
    client_name = serializers.CharField(max_length=50)


    class Meta:
        model = Invoices
        fields = "__all__"