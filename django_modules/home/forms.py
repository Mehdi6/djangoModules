from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(required=True, min_length=5, max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    subject = forms.CharField(required=False, min_length=5, max_length=140, label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    content = forms.CharField(required=True, max_length=2500, label='Content', widget=forms.Textarea)
    
    def send_email(self):
        
        pass