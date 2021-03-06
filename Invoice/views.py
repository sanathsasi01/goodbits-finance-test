from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import Invoice_Serializer
from rest_framework import status
import stripe
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
stripe.api_key = settings.STRIPE_KEY


@api_view(['POST',])
@permission_classes((AllowAny,))
def add_invoice(request):
    # get email and amount from request.data
    client_email = request.data.get('client_email', None)
    client_name = request.data.get('client_name', None)
    amount = request.data.get('amount', None)

    serializer = Invoice_Serializer(data=request.data)

    # validation the serializer and save
    if serializer.is_valid():
        payment_instance = stripe.PaymentIntent.create(
            amount=amount,
            currency='inr',
            payment_method_types=['card'],
        )
        serializer.save()
        # not sure if this is the payment link (didnt see another url).
        url = payment_instance['charges']['url']
        
        # send an email to client_email with the url from stripe
        html_content = render_to_string('Emails/paymentLink.html', {
            'client_name' : client_name,
            'url' : url,
        })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives("Payment Link", text_content, settings.EMAIL_HOST_USER, [client_email])
        email.attach_alternative(html_content, "text/html")
        try:
            email.send() #it was working but the account was disabled my google(email functionality may not work).
        except Exception as e:
            print(e)
            
        return Response({'success' : 'email with paymentlink sent successfully'})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
