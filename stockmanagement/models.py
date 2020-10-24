from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    quantity = models.CharField(max_length=50, null=False, blank=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-date_created']
        
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False, unique=False)
    item = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(blank=True, null=True, default="N/A")
    phone = models.CharField(max_length=60, blank=False, null=False)
    city = models.CharField(max_length=120, blank=False, null=False)
    country = models.CharField(max_length=120, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name
    

class AddStockItem(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    subcat = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120, blank=False, null=False, unique=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=0)
    unit = models.CharField(max_length=100, blank=True, null=True, default='')
    status = models.CharField(max_length=40, blank=False, null=False, default='Normal')
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        unique_together = (('cat', 'subcat', 'name'),)
        ordering = ['-date_created']
    
    def __str__(self):
        return self.name

