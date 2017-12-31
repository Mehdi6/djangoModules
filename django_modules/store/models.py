from django.db import models
from ..users.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_rate(value):
    if value > 5 or value < 0:
        raise ValidationError(
            _('%(value)s is not between 0 and 5'),
            params={'value': value},
        )

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    instock = models.BooleanField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, default='SLUG DEFAULT')
    
    def __str__(self):
        return self.name
        
class Brand(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_cat = models.ForeignKey('Category', null=True, blank=True)
    slug = models.SlugField(max_length=50, default="SLUG DEFAULT")
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(validators=[validate_rate])
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.title
        
class ProductMedia(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    isPrimary = models.BooleanField()

    