"""
URL configuration for happyhoegrocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kgl import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('sample/', views.sample, name='sample'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    #you tell django to ive you the functionality for authentication "functionality to log in".this is the Login for the sales agent.
    path('login/', auth_views.LoginView.as_view(template_name='kgl/login.html'), name = 'login'),
    path('logout/', auth_views.LoginView.as_view(template_name='kgl/logout.html'), name = 'logout'),
    path('home/<int:product_id>/',views.product_detail, name = 'product_detail'),
    path('delete/<int:product_id>/',views.delete_detail, name = 'delete_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('all_sales/', views.all_sales, name='all_sales'),
    path('deffered_payments/', views.deffered_payments, name='deffered_payments'),
    path('deffered_payments_list/', views.deffered_payments_list, name='deffered_payments_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('receipt_detail/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('record_sales/', views.record_sales, name='record_sales'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)