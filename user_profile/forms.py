from django import forms
from django.contrib.auth.models import User

from user_profile.models import Profile

class UserInfoForm(forms.ModelForm):
  username = forms.CharField(
    required=False,
    max_length=100,
    widget=forms.TextInput()
  )
  first_name = forms.CharField(
    required=False,
    max_length=100,
    widget=forms.TextInput()
  )
  last_name = forms.CharField(
    required=False,
    max_length=100,
    widget=forms.TextInput()
  )

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name']


class ProfileCreateUpdateForm(forms.ModelForm):
  phone_number = forms.CharField(
    required=True,
  )
  location = forms.CharField(
    required=True
  )
  address = forms.CharField(
    required=True
  )
  birth_date = forms.CharField(
    required=True,
    widget=forms.SelectDateWidget()
  )
  class Meta:
    model = Profile
    fields = ['phone_number', 'location', 'address', 'birth_date']