from django.shortcuts import render

from .models import Transaction
from crm.models import Order


def orders(request):
    orders_count = Order.objects.all().count()
    payed_orders_count = Order.objects.filter(state=8).count()
    on_the_way_orders = Order.objects.filter(state=6).count()
    in_department_orders = Order.objects.filter(state=7).count()
    refused_orders = Order.objects.filter(state=9).count()
    percent_refused_orders = refused_orders / (orders_count / 100)
    waitlist_orders_count = Order.objects.filter(state__range=[4, 5]).count()

    return render(request, 'analytics/orders.html',
                  {'payed_orders_count': payed_orders_count,
                   'orders_count': orders_count,
                   'on_the_way_orders': on_the_way_orders,
                   'in_department_orders': in_department_orders,
                   'refused_orders': refused_orders,
                   'percent_refused_orders': percent_refused_orders,
                   'waitlist_orders_count': waitlist_orders_count})


def money(request):
    expenses = Transaction.objects.filter(type=1)
    incomes = Transaction.objects.filter(type=2)
    payed_orders = Order.objects.filter(state=8)

    payed_orders_sum = 0
    for payed_order in payed_orders:
        payed_orders_sum += payed_order.sum
    expenses_sum = 0
    for expense in expenses:
        expenses_sum += expense.sum
    incomes_sum = 0
    for income in incomes:
        incomes_sum += income.sum
    balance = incomes_sum - expenses_sum

    return render(request, 'analytics/money.html',
                  {'balance': balance,
                   'payed_orders_sum': payed_orders_sum,
                   })
