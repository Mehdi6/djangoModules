from django.contrib import admin
from .models import Category 

# Register your models here.
@admin.register(Category)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_cat']
