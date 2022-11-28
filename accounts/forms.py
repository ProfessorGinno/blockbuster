from django import forms
from .models import UserProfile


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'Placeholder':'Email'}) )
    first_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'Placeholder': 'First name'}))
    last_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'Placeholder': 'Last name'}))
    phone = forms.CharField(label='', max_length=20, required=False, widget=forms.TextInput(attrs={'Placeholder':'Mobile Number'}))
    address = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder':'Address Line'}))
    country = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder': 'Country'}))
    state= forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder':'State/Region'}))
    city = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder': 'City'}))
    imagen = forms.ImageField(label='Imagen', required=False)

"""  class Meta:
       model = UserProfile
       fields = ('email', 'first_name', 'last_name', 'phone', 'address', 'country', 'state', 'city', 'image')
       widgets = {
           'email': forms.TextInput(attrs={'Placeholder':'Email'}),
           'first_name': forms.TextInput(attrs={'Placeholder': 'First name'}),
           'last_name': forms.TextInput(attrs={'Placeholder': 'Last name'}),
           'phone': forms.TextInput(attrs={'Placeholder':'Mobile Number'}),
           'address': forms.TextInput(attrs={'Placeholder':'Address Line'}),
           'country': forms.TextInput(attrs={'Placeholder': 'Country'}),
           'state': forms.TextInput(attrs={'Placeholder':'State/Region'}),
           'city': forms.TextInput(attrs={'Placeholder': 'City'}),
       }
       
       labels = {
           'email': "",
           'first_name': "",
           'last_name': "",
           'phone': "",
           'address': "",
           'country': "",
           'state': "",
           'city': "",
       } """