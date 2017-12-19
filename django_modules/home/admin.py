from django.contrib import admin
from .models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'title', 'picture']