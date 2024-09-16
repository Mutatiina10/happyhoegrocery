from django.contrib import admin
from .models import Stockx, Sale, Deffered_payments
# Register your models here.

admin.site.register(Stockx)
admin.site.register(Sale)
admin.site.register(Deffered_payments)
