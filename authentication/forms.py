# from django import forms
# from .models import UserAccount

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = UserAccount
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']