from django.contrib import admin

# Register your models here.

from .models import Ficheiros,MyUser

admin.site.register(Ficheiros)
admin.site.register(MyUser)