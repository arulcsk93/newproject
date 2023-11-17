from django.contrib import admin
from .models import *


class Registerdata(admin.ModelAdmin):
    list_display = ('Name', 'Mobile')


admin.site.register(Register, Registerdata)
