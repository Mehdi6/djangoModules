from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import datetime
from enum import Enum


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
	
    female = "F"
    male = "M"
    
    genders = ((female, "female"), (male, "male"))
    
    gender = models.CharField(choices=genders, default=female, max_length= 20, blank=True)
	
    birth_date = models.DateField(blank=True, default=datetime.date.min)
	
    phone = models.CharField(max_length = 20, blank=True, default="")
	
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
