from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            'class': 'input100',
            'placeholder': 'Type your password'
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'input100',
            'placeholder': 'Type your password'
        })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Type your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Type your last name'}),
            'username': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Type your username'}),
            'email': forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Type your email'}),
            # 'password1': forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Type your password'}),
            # 'password2': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Type your password again'})
        }
