from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Очистить количество товара")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    '''Список продкуктов, для того чтобы вносить изменения в админке, база данных не изменится'''
    list_display = ['name', 'email', 'address', 'date_reg']
    ordering = ['-name']  # автоматичекска сортировка в админке
    list_filter = ['address']  # добавление фильтра
    search_fields = ['name']

    readonly_fields = ['name', 'date_reg']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'date_reg'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],  # поле должно быть схлопнуто
                'description': 'Информация о клиенте',
                'fields': ['email', 'phone', 'address'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'total_price', 'date_ordered']
    ordering = ['-customer']  # автоматичекска сортировка в админке
    list_filter = ['product']  # добавление фильтра
    search_fields = ['product']

    readonly_fields = ['customer', 'date_ordered']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer', 'date_ordered'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],  # поле должно быть схлопнуто
                'description': 'Информация о заказе',
                'fields': ['product', 'total_price'],
            },
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'date_in', 'img_file']
    ordering = ['-name']  # автоматичекска сортировка в админке
    list_filter = ['name']  # добавление фильтра
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    readonly_fields = ['name', 'date_in']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Описание продукта',
            {
                'classes': ['collapse'],  # поле должно быть схлопнуто
                'description': 'О продукте',
                'fields': ['description'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'description': 'Информация о продукте',
                'fields': ['price', 'quantity', 'date_in', 'img_file'],
            },
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
