from django.contrib import admin
from .models  import Xodim
# Register your models here.

@admin.register(Xodim)
class XodimAdmin(admin.ModelAdmin):
    list_display = ['name','age','department','salary']
    search_fields = ['name']
    list_filter = ['department','city','position']
    