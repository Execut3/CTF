from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username here'}), label='Username: ')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password here', 'type': 'password'}),
                               label='Password: ')


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username here'}), label='Username: ')
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password here', 'type': 'password'}),
                               label='Password: ')
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email here'}), label='Email: ')

