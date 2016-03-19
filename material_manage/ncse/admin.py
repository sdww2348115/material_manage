from django.contrib import admin

# Register your models here.
from .models import UserGroup
from .models import User
from .models import Apply
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'borrow_status', 'borrow_id', 'create_time', 'modify_time')
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'passwd', 'group', 'authority', 'name')
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user', 'detail', 'apply_status', 'bought_status', 'create_time', 'modify_time')

admin.site.register(UserGroup)
admin.site.register(User, UserAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(Item, ItemAdmin)
