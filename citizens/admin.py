from django.contrib import admin

from .models import Citizen, Passport, Manager, History
# Register your models here.
admin.site.register(Passport)
admin.site.register(Citizen)
admin.site.register(Manager)
admin.site.register(History)