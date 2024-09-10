from django.forms import ModelForm
from .models import *


class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['branch_name', 'seller', 'issued_to', 'quantity', 'unit_price', 'amount_received']


class Deffered_paymentsForm(ModelForm):
    class Meta:
        model = Deffered_payments
        fields = '__all__'
        
class StockxForm(ModelForm):
    class Meta:
        model = Stockx
        fields = '__all__'

class AddForm(ModelForm):
    class Meta:
        model = Stockx
        fields = ['total_quantity']