from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.IMS)
admin.site.register(models.History_IMS)