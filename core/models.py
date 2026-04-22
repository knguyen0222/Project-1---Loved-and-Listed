from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    CATEGORY_CHOICES = [
        ('Shoes', 'Shoes'),
        ('Clothing', 'Clothing'),
        ('Outerwear', 'Outerwear'),
        ('Handbag', 'Handbag'),
        ('Accessory', 'Accessory'),
        ('Jewelry', 'Jewelry'),
        ('Makeup', 'Makeup'),
        ('Other', 'Other'),
    ]

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Like New', 'Like New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
    ]

    STATUS_CHOICES = [
        ('Keeping', 'Keeping'),
        ('Listed', 'Listed'),
        ('Sold', 'Sold'),
    ]

    PLATFORM_CHOICES = [
        ('Depop', 'Depop'),
        ('Poshmark', 'Poshmark'),
        ('Mercari', 'Mercari'),
        ('eBay', 'eBay'),
        ('Other', 'Other'),
    ]

    item_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acquired_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Keeping')
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, blank=True, null=True)
    sold_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def profit(self):
        if self.sold_price and self.purchase_price:
            return self.sold_price - self.purchase_price
        return None

    def __str__(self):
        return self.item_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name

class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item', 'tag')