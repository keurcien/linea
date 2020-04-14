from django.contrib import admin

# Register your models here.
from .models import User, Weight

class WeightAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'date']
    list_filter = ['user']

admin.site.register(User)
admin.site.register(Weight, WeightAdmin)