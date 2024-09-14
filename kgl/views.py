from django.shortcuts import render,redirect, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .filters import StockxFilter
#accessing our models so that we can get content out oof them.
from .models import * #(* assitaris means"all" or write all the models you created by listing them with commas)
#borrowing decorators from django to restrict access to our pages.
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
# Create your views here.
def index(request):
    products = Stockx.objects.all().order_by('-id')
    return render(request,"kgl/index.html", {'products': products})

def sample(request):
    products = Stockx.objects.all()
    return render(request,"kgl/sample.html", {'product': products})


@login_required
def home(request): 
    #for the search
    products = Stockx.objects.all().order_by('-id')
    product_filters = StockxFilter(request.GET, queryset = products)
    products = product_filters.qs
    return render(request,"kgl/home.html", {'products':products,'product_filters': product_filters})

def register(request):
    return render(request,"kgl/register.html")
@login_required
def logout(request):
    return render(request,"kgl/logout.html")


@login_required
def product_detail(request, product_id):
    product = Stockx.objects.get(id = product_id)
    return render(request,"kgl/product_detail.html", {'product': product})


@login_required
def delete_detail(request, product_id):
    product = Stockx.objects.get(id = product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def issue_item(request,pk):
    #accessing all items in the stock model
    issued_item = Stockx.objects.get(id = pk)
    #accessing our form 
    sales_form = SaleForm(request.POST)
    #receiving data from the form and saving from the model


    if request.method == 'POST':
        #checking whether the form is valid
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keep track of sales remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt')

    return render(request, 'kgl/issue_item.html',{'sales_form':sales_form})

        
@login_required
def log_out(request):
    logout(request)
    return redirect('/')



@login_required
def receipt(request):
    sales = Sales.objects.all().order_by('-id')
    return render(request,'kgl/receipt.html', {'sales': sales})



@login_required
def receipt_detail(request, receipt_id):
    receipt = Sales.objects.get(id=receipt_id)
    return render(request, 'kgl/receipt_detail.html', {'receipt':receipt})


@login_required
def all_sales(request):
    sales = Sales.objects.all().order_by('-id')
    total_expected = sum([items.get_total() or 0  for items in sales])
    total = sum([items.amount_received or 0 for items in sales])
    total_change = sum([items.get_change() or 0  for items in sales])
    net = total_expected - total
    return render(request, 'digitalbook/all_sales.html', {'sales': sales, 'total':total, 'total_change':total_change, 'net':net, 'total_expected':total_expected})

def deffered_payments(request):
    if request.method == 'POST':
        form = Deffered_paymentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Deffered_paymentsForm()
        return render(request, 'kgl/deffered_payments.html', {'form': form})

def deffered_payments_list(request):
    payment = Deffered_payments.objects.all().order_by('-id')
    return render(request, 'kgl/deffered_payments_list.html', {'payments': payment})


def add_product(request):
    if request.method == 'POST':
        form = StockxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StockxForm()
        return render(request, 'kgl/add_product.html', {'form': form})
    
@login_required
def record_sales(request):
    if request.method == 'POST':
        sales_form = SaleForm(request.POST)
        
        if sales_form.is_valid():
            # Get the specific item from the form data
            item_id = request.POST.get('item')
            issued_item = Stockx.objects.get(id=item_id)

            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item  # Assign the specific Stockx instance
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()

            # Keep track of sales remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('all_sales')

    else:
        sales_form = SaleForm()

    return render(request, 'kgl/record_sales.html', {'sales_form': sales_form})

@login_required
def add_to_stock(request, pk):
    # creating the variable which will access all the objects
    issued_item = Stockx.objects.get(id=pk)
    # creating a form to be used to post out data to be saved to the database
    form = AddForm(request.POST)
    if request.method == 'POST':
        # confirming that if some submits to send the submiiting request, 
        # if the form is valid , proceed 
        if form.is_valid():
            # filtering the field posted from the form is converted to interger and gv to da added quantity variable
            added_quantity = int(request.POST['total_quantity'])
            # here were adding the quantity coming from the form and add it wz da value currently in the database"issued_total_quantity"
            issued_item.total_quantity += added_quantity
            # saving the results got after addding the added quantity
            issued_item.save()
            # used for debugging , to print the actual values in the terminal"nt so crucial".
            print(added_quantity)
            print(issued_item.total_quantity)
            # going baclk to our home to continue.
            return redirect('home')
    #   help us render our data  # 
    return render(request, 'kgl/add_to_stock.html', {'form':form})
