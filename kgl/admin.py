from django.contrib import admin
from .models import Stockx, Sales, Deffered_payments
# Register your models here.

admin.site.register(Stockx)
admin.site.register(Sales)
admin.site.register(Deffered_payments)
