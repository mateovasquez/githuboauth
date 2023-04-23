from django import forms
from django.contrib.auth.models import User

from user_profile.models import Profile

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


class ProfileEditForm(forms.ModelForm):
  phone_number = forms.CharField(
    max_length=9,
    min_length=9,
  )
  birth_date = forms.CharField(
    widget=forms.SelectDateWidget()
  )

  class Meta:
    model = Profile
    fields = ['phone_number', 'location', 'address', 'birth_date']

class ProfileCreateForm(ProfileEditForm):
  phone_number = forms.CharField(
    required=True,
    max_length=9,
    min_length=9,
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