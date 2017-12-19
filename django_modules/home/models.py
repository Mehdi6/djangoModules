from django.db import models
from django.contrib import admin

# Create your models here.
class Testimonial(models.Model):
    
    content = models.TextField(help_text='Content of the testimonial')
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='testimonials')

    def __str__(self):
        return self.title
        