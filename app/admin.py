from django.contrib import admin
from app.models import Connection, ClientCompany, ServiceContact


# Register your models here.
@admin.register(Connection)
class AdminConnection(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email')
    list_display_links = ('id', 'full_name', 'phone', 'email')
    list_filter = ('full_name',)


@admin.register(ClientCompany)
class AdminClientCompany(admin.ModelAdmin):
    list_display = ('full_name', 'image', 'position', 'type')
    list_display_links = ('full_name', 'image', 'position', 'type')


@admin.register(ServiceContact)
class AdminServiceContact(admin.ModelAdmin):
    list_display = ('connection', 'service', 'category')
    list_display_links = ('connection', 'service', 'category')
