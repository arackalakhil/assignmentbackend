from django.contrib import admin

from accounts.models import Account
from accounts.models import App
from accounts.models import completedTask
# Register your models here.
admin.site.register(Account)
admin.site.register(App)
admin.site.register(completedTask)
