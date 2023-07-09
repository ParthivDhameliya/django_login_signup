from django import forms
from .models import registrationModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class userSignup(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mobile_number = forms.CharField(required=True, max_length=10,
                                    widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = registrationModel
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_mobile_number(self):
        mn = self.cleaned_data['mobile_number']
        if 0 < len(mn) < 10:
            raise forms.ValidationError("Mobile number should be 10 numbers long")
        for i in mn:
            if not i.isdigit():
                raise forms.ValidationError("Mobile number should only contain numbers")
        return mn


class userLogin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False,
                               widget=forms.PasswordInput(
                                   attrs={"autocomplete": "current-password", 'class': 'form-control'}))
