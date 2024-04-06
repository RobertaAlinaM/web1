from django.contrib import admin

# This is how you can register your models with the Django admin so that you can manage them from the admin interface

from .models import Transport, Passenger, Ticket, Pollution

admin.site.register(Transport)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(Pollution)
