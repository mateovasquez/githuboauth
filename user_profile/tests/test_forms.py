import pytest
from user_profile.forms import ProfileCreateUpdateForm, UserInfoForm

@pytest.mark.django_db
class TestUserForm():
  def test_form_is_valid_all_fields(self):
    form_data = {
      "username": "wolfandbadger",
      "first_name": "wolf",
      "last_name": "badger",
    }
    form = UserInfoForm(data=form_data)
    assert form.is_valid() == True
  
  def test_form_is_valid_some_fields(self):
    form_data = {"first_name": "wolf"}
    form = UserInfoForm(data=form_data)
    assert form.is_valid() == True

@pytest.mark.django_db
class TestProfileForm():
  def test_form_is_valid(self):
    form_data = {
      'phone_number': '+34666666666', 
      'address': 'fake street 123',
      'location': 'somewhere',
      'birth_date': '2023-04-23',
    }
    form = ProfileCreateUpdateForm(data=form_data)
    assert form.is_valid() == True

  def test_form_not_valid_missing_fields(self):
    form = ProfileCreateUpdateForm(data={})
    assert form.is_valid() == False
    assert form.errors['phone_number'] == ['This field is required.']
    assert form.errors['address'] == ['This field is required.']
    assert form.errors['location'] == ['This field is required.']
    assert form.errors['birth_date'] == ['This field is required.']

  def test_form_invalid_phone_number(self):
    invalid_phone_number = '666666666'
    form_data = {
      'phone_number': invalid_phone_number,
      'address': 'fake street 123',
      'location': 'somewhere',
      'birth_date': '2023-04-23',
    }
    form = ProfileCreateUpdateForm(data=form_data)
    print(dict(form.errors))
    assert form.is_valid() == False
    assert form.errors['phone_number'] == ["Phone number must be entered in the format: '+999999999'. From 9 to 15 digits allowed."]

  def test_form_invalid_birth_date(self):
    invalid_birth_date = 'today'
    form_data = {
      'phone_number': '+34666666666',
      'address': 'fake street 123',
      'location': 'somewhere',
      'birth_date': invalid_birth_date,
    }
    form = ProfileCreateUpdateForm(data=form_data)
    assert form.is_valid() == False
    assert form.errors['birth_date'] == ['“today” value has an invalid date format. It must be in YYYY-MM-DD format.']