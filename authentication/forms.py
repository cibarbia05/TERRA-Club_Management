from django import forms
from django.contrib.auth import password_validation

from authentication.models import User


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean(self):
        pass
        # if not "@students.dadeschools.net" in self.cleaned_data['email']:
        #     raise forms.ValidationError('Enter a valid school issued email')


#         validate id in excel sheet


class SignInForm(forms.Form):
    id = forms.CharField(label="Student ID")
    password = forms.CharField(label="Password")

    def clean(self):
        pass


class PasswordForgotEmail(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Email'}))

    def clean(self):
        if not User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('No user has the provided email')


class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'id': 'password1'}),
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'id': 'password2'}),
    )

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        password_validation.validate_password(self.cleaned_data.get('password'), None)
