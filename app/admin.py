from django.contrib import admin
from .models import *
from app.models import Connection, ClientCompany, ServiceContact


admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Info)
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
