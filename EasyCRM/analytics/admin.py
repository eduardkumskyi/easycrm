from django.contrib import admin
from .models import Transaction, Purpose


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'purpose', 'sum', 'date', 'comment', 'project' ]
    list_filter = ['project', 'date', 'type', 'purpose']
    readonly_fields = ['user']
    verbose_name = "Транзакция"
    verbose_name_plural = "Транзакции"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']
    readonly_fields = ['user']
    verbose_name = "Назначение транзакции"
    verbose_name_plural = "Назначения транзакций"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
