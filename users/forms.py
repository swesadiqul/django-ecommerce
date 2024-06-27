from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



#create forms here
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'agree_to_terms']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput)
    email_addess = forms.CharField(widget=forms.EmailInput)
    phone = forms.CharField(widget=forms.TextInput)
    dob = forms.DateField(widget=forms.DateInput)
    address1 = forms.CharField(widget=forms.TextInput)
    address2 = forms.CharField(widget=forms.TextInput)
    country = CountryField()
    city = forms.CharField(widget=forms.TextInput)
    post_code = forms.CharField(widget=forms.TextInput)
    image = forms.ImageField(widget=forms.ClearableFileInput)


    widgets = {"country": CountrySelectWidget()}





