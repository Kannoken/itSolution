from django.contrib import admin
from SpaceApp.models import MsgFromSpace


# Register your models here.

class MsgAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsgFromSpace, MsgAdmin)
