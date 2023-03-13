from .models import Order
from django.core.mail import send_mail
from django.conf import settings


def update_stock(products, quantities):
    for item in range(len(products)):
        product = products[item]
        quantidade = quantities[item]
        product_obj = Order.objects.get(id=product.id)
        if product_obj.stock < quantidade:
            raise ValueError(f'O produto {product_obj.name} está indisponível.')
        product_obj.stock -= quantidade
        product_obj.save()


def send_email_user(order):
    subject = 'Order updated'
    message = f'Your order with ID {order.id} has been updated. New status: {order.status}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.user.email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
