from django import forms
from django.contrib.auth.models import User

class UserInfoForm(forms.ModelForm):
  username = forms.CharField(
    max_length=100,
    widget=forms.TextInput()
  )
  first_name = forms.CharField(
    max_length=100,
    widget=forms.TextInput()
  )
  last_name = forms.CharField(
    max_length=100,
    widget=forms.TextInput()
  )

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name']