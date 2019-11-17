from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30, help_text='Username should contain no spaces')
    email = forms.EmailField(label='Email address' , widget=forms.EmailInput)
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=6 , help_text='Password at least 6 digit')
    password2 = forms.CharField(label='Confrim password', widget=forms.PasswordInput(), min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password not matches')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Username already taken')
        return cd['username']

class LogiForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=('username','password')