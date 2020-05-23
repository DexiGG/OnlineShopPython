from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order {order.id}'
    mail_sent = send_mail(subject, 'admin@mail.ru', [order.email])
    return mail_sent
