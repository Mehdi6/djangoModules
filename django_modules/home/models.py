from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class Testimonial(models.Model):
    
    content = models.TextField(help_text='Content of the testimonial')
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='testimonials')

    def __str__(self):
        return self.title
 
class Contact(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=140, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name