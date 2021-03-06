from django.contrib import admin
from .models import Order, Project


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'waybill', 'state', 'sum', 'payed_sum', 'project', 'create_date']
    fields = ['first_name', 'last_name', 'middle_name', 'phone',
              'city', 'department', 'waybill', 'order', 'comment',
              'state', 'sum', 'payed_sum', 'project', 'create_date',
              'update_date', 'no_send_messages', 'message_1', 'message_2', 'message_3', 'user']
    readonly_fields = ['update_date', 'user', 'message_1', 'message_2', 'message_3']
    list_filter = ['create_date', 'update_date', 'state']
    verbose_name = "Заказ"
    verbose_name_plural = "Заказы"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['user']
    verbose_name = "Проект"
    verbose_name_plural = "Проекты"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
