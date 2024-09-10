import django_filters
from .models import Stockx

class StockxFilter(django_filters.FilterSet):
    class Meta:
        model = Stockx
        fields = ['item_name']