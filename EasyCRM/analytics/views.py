from django.shortcuts import render

from .models import Transaction
from crm.models import Order


def index(request):
    orders_count = Order.objects.all().count()
    waitlist_orders_count = Order.objects.filter(state__range=[4, 5]).count()
    expenses = Transaction.objects.filter(type=1)
    incomes = Transaction.objects.filter(type=2)

    expenses_sum = 0
    incomes_sum = 0
    for expense in expenses:
        expenses_sum += expense.sum
    for income in incomes:
        incomes_sum += income.sum
    balance = incomes_sum - expenses_sum
    return render(request, 'analytics/index.html',
                  {'balance': balance, 'orders_count': orders_count,
                   'waitlist_orders_count': waitlist_orders_count})
