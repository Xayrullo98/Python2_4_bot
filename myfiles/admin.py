from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type,AdminType)


class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','tur','rasm','text']
admin.site.register(Maxsulot,AdminMax)

class AdminKorzinka(admin.ModelAdmin):
    list_display = ['id',"ism",'tg_id','nomi','narxi','son']
admin.site.register(Korzinka,AdminKorzinka)


class AdminMenu(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu,AdminMenu)



class AdminUser(admin.ModelAdmin):
    list_display = ['id','ism','fam','username','tg_id','date']
admin.site.register(Azolar,AdminUser)