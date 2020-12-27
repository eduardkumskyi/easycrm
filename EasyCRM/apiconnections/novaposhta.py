import math
import requests

from apiconnections.TurboSMS import turbosms_notification
from crm.models import Order, Project


def np_state_update(np_api_key="", documents_ready="", turbosms_sender="", turbosms_api=""):
    url = "https://api.novaposhta.ua/v2.0/json/"
    payload = {
          'apiKey': np_api_key,
          'modelName': 'TrackingDocument',
          'calledMethod': 'getStatusDocuments',
          'methodProperties': {
              'Documents': documents_ready
          }
      }
    headers = {
        'Content-Type': 'string',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    status_codes = {}
    for i in response.json()['data']:
        status_code = i['StatusCode']
        if 1 <= int(status_code) <= 3:
            pass
        elif 4 <= int(status_code) <= 6:
            status_codes.setdefault(i['Number'], 6)
        elif 7 <= int(status_code) <= 8:
            status_codes.setdefault(i['Number'], 7)
        elif 9 <= int(status_code) <= 11:
            status_codes.setdefault(i['Number'], 8)
        else:
            pass
    return state_update(status_codes, turbosms_sender, turbosms_api)


def state_update(status_codes, turbosms_sender, turbosms_api):
    for waybill, state in status_codes.items():
        order = Order.objects.get(waybill=waybill)
        order.state = state
        order.save()
        if turbosms_api != "":  # SMS NOTIFICATION
            if state == 6 and order.message_1 == "-" and order.no_send_messages is False:
                turbosms_notification(order.phone, turbosms_sender,
                                      f"Ваш заказ отправлен, номер ТТН:{order.waybill}", turbosms_api)
                order = Order.objects.get(id=order.id)
                order.message_1 = "Отправлено"
                order.save()
            elif state == 7 and order.message_2 == "-" and order.no_send_messages is False:
                turbosms_notification(order.phone, turbosms_sender,
                                      f"Ваш заказ уже в отделении, период хранения 5 дней.", turbosms_api)
                order = Order.objects.get(id=order.id)
                order.message_2 = "Отправлено"
                order.save()
            elif state is None:
                pass


def np_state_update_all(step=100):
    for project in Project.objects.exclude(np_api=''):
        turbosms_sender = project.turbosms_sender
        turbosms_api = project.turbosms_api
        orders = Order.objects.filter(waybill__isnull=False, project=project)
        iterations = math.ceil(orders.count() / step)
        for i in range(0, iterations):
            start, end = step * i, step * i + step
            documents = [
                {'DocumentNumber': str(waybill), 'Phone': ''}
                for waybill in orders[start:end].values_list('waybill', flat=True)
            ]
            np_state_update(project.np_api, documents, turbosms_sender, turbosms_api)
    print("Статусы обновлены.")
