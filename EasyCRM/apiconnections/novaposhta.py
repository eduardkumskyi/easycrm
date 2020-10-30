import datetime

import requests

from apiconnections.TurboSMS import turbosms_notification
from projects.models import Project
from orders.models import Order


def np_status_update(np_api_key="", waybill=""):

    url = "https://api.novaposhta.ua/v2.0/json/"

    payload = {
          'apiKey': np_api_key,
          'modelName': 'TrackingDocument',
          'calledMethod': 'getStatusDocuments',
          'methodProperties': {
              'Documents': [
                  {
                      'DocumentNumber': waybill,
                      'Phone': ''
                  }
              ]
          }
      }

    headers = {
        'Content-Type': 'string',
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    status_code = response.json()['data'][0]['StatusCode']

    if 1 <= int(status_code) <= 3:
        pass
    elif 4 <= int(status_code) <= 6:
        return 6
    elif 7 <= int(status_code) <= 8:
        return 7
    elif 9 <= int(status_code) <= 11:
        return 8
    else:
        pass


def np_status_update_all():
    for project in Project.objects.all():
        for order in Order.objects.filter(project=project.id):
            if project.np_api == "" or order.waybill == "":
                pass
            else:
                if project.np_api is None or order.waybill is None:
                    pass
                else:
                    new_state = np_status_update(str(project.np_api), str(order.waybill))
                    if new_state == 6 and order.message_1 is False:
                        turbosms_notification(order.phone, project.turbosms_sender,
                                              f"Ваш заказ отправлен, номер ТТН:{order.waybill}", project.turbosms_api)
                        order = Order.objects.get(id=order.id)
                        order.message_1 = True
                        order.save()
                    elif new_state == 8 and order.message_2 is False:
                        turbosms_notification(order.phone, project.turbosms_sender,
                                              f"Ваш заказ уже в отделении, период хранение 5 дней.", project.turbosms_api)
                        order = Order.objects.get(id=order.id)
                        order.message_2 = True
                        order.save()
                    elif new_state is None:
                        pass
                    else:
                        order = Order.objects.get(id=order.id)
                        order.state = new_state
                        order.save()
    print("Все статусы успешно обновлены.")
