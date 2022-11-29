from django import forms


class UserEditForm(forms.Form):

    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'Placeholder':'Email'}) )
    first_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'Placeholder': 'First name'}))
    last_name = forms.CharField(label='', max_length=30, required=False, widget=forms.TextInput(attrs={'Placeholder': 'Last name'}))
    phone = forms.CharField(label='', max_length=20, required=False, widget=forms.TextInput(attrs={'Placeholder':'Mobile Number'}))
    address = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder':'Address Line'}))
    country = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder': 'Country'}))
    state= forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder':'State/Region'}))
    city = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'Placeholder': 'City'}))
    image = forms.ImageField(label='Imagen', required=False)


