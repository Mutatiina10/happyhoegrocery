from django import forms
from django.forms import ModelForm
from .models import *


class SaleForm(ModelForm):
    branch_name = forms.CharField(required=True)
    seller = forms.CharField(required=True)
    issued_to = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True)
    unit_price = forms.IntegerField(required=True)
    amount_received = forms.IntegerField(required=True)

    class Meta:
        model = Sale
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