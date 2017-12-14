from django import forms

class SignupForm(forms.Form):
    
    female = "F"
    male = "M"

    genders = ((female, "female"), (male, "male"))
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	
    gender = forms.ChoiceField(choices=genders)
	
    date_of_birth = forms.DateField(label="Date of birth", widget=forms.TextInput(attrs={'placeholder': 'Date of birth', "data-provide":"datepicker"}))
	
    phone = forms.CharField(max_length=20, label="Phone", widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.phone = self.cleaned_data['phone']
        
        user.save()