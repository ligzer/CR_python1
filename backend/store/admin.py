from django.contrib import admin

# Register your models here.

from .models import Store, Street, Schedule, Town


admin.site.register(Town, admin.ModelAdmin)
admin.site.register(Street, admin.ModelAdmin)
admin.site.register(Schedule, admin.ModelAdmin)
admin.site.register(Store, admin.ModelAdmin)
