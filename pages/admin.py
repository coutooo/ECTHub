from django.contrib import admin

# Register your models here.

from .models import Ficheiros,User

admin.site.register(Ficheiros)
admin.site.register(User)