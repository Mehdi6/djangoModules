from django.contrib import admin
from .models import Testimonial, Contact

# Register your models here.
@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'title', 'picture']
    
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'email', 'subject', 'content']
    readonly_fields = ['created_at', 'name', 'email', 'subject', 'content']
    