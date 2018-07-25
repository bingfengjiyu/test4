from django.contrib import admin
from LoginInfo.models import UserInfo
# Register your models here.


class LoginInfoAdmin(admin.ModelAdmin):
    list_display = ["id","username","password","phone"]


admin.site.register(UserInfo,LoginInfoAdmin)