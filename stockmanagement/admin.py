from django.contrib import admin
from stockmanagement.models import Category, SubCategory, Supplier, AddStockItem


admin.site.register((Category,SubCategory,Supplier,AddStockItem,))
