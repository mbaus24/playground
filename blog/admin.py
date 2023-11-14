from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Character, Equipement
 
admin.site.register(Character)
admin.site.register(Equipement)