from django import forms
from .models import Contact
from django.core.mail import EmailMessage
from django.conf import settings

class ContactForm(forms.Form):
    
    name = forms.CharField(required=True, min_length=3, max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    subject = forms.CharField(required=False, min_length=3, max_length=140, label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(required=True, max_length=2500, label='Content', widget=forms.Textarea)
    
    def send_email(self):
        email = EmailMessage(self.cleaned_data['name'] +' - SUBJECT:'+self.cleaned_data['subject'],\
                     'EMAIL: '+self.cleaned_data['email'] +'\nCONTENT: '+self.cleaned_data['content'],\
                            to=settings.ADMINS_EMAILS)
        email.send()
        pass
    
    def save(self):
        contact = Contact(name=self.cleaned_data['name'], email=self.cleaned_data['email'],\
                              subject=self.cleaned_data['subject'], content=self.cleaned_data['content'])
        contact.save()
        