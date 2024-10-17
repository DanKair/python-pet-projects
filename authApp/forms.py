from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')

            # Check if the passwords matches
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Passwords Doesn't Match!")

            return cleaned_data
