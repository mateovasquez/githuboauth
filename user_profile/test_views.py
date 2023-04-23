import pytest
from datetime import datetime

from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from user_profile.models import Profile

@pytest.mark.django_db
class TestGetPostUser(TestCase):
  user_url = reverse('user_detail')

  def test_get_user_info(self):
    user = User.objects.create(
      username='wolf&badger',
      first_name='wolf',
      last_name='badger'
    )
    self.client.force_login(user=user)
    response = self.client.get(self.user_url)

    response_data = response.context['user_form'].__dict__['initial']
    assert response_data['username'] == user.username
    assert response_data['first_name'] == user.first_name
    assert response_data['last_name'] == user.last_name

    user.delete()

  def test_post_user_info(self):
    user = User.objects.create(
      username='wolf&badger',
      first_name='wolf',
      last_name='badger',
      email="wolf@badger.com",
    )
    body = {
      'username': 'test',
      'first_name': 'test_first',
      'last_name': 'test_last',
      'email': 'test@email.com' #not included in form fields
    }
    self.client.force_login(user=user)
    self.client.post(self.user_url, body)
    user.refresh_from_db()

    assert user.username == 'test'
    assert user.first_name == 'test_first'
    assert user.last_name == 'test_last'
    assert user.email == 'wolf@badger.com'

    user.delete()

@pytest.mark.django_db
class TestGetProfile(TestCase):
  profile_detail_url = reverse('profile_detail')

  def test_get_profile_info(self):
    user = User.objects.create()
    profile = Profile.objects.create(
      user=user,
      phone_number='666666666', 
      address='fake street 123', 
      location='somewhere', 
      birth_date='2023-04-23', 
    )

    self.client.force_login(user=user)
    response = self.client.get(self.profile_detail_url)
    response_content = str(response.content, encoding='utf8')

    birthday_date = datetime.strptime(profile.birth_date, '%Y-%m-%d')
    birthday_date = birthday_date.strftime('%B %d, %Y')
    assert birthday_date in response_content
    assert profile.phone_number in response_content
    assert profile.address in response_content
    assert profile.location in response_content

    profile.delete()
    user.delete()

@pytest.mark.django_db
class TestCreateUpdateProfile(TestCase):
  profile_edit_url = reverse('profile_edit')

  def test_update_profile_info(self):
    user = User.objects.create()
    profile = Profile.objects.create(user=user)
    body = {
      'phone_number': '666666666', 
      'address': 'fake street 123', 
      'location': 'somewhere', 
      'birth_date': '2023-04-23', 
    }

    self.client.force_login(user=user)
    self.client.post(self.profile_edit_url, body)

    profile.refresh_from_db()
    assert profile.phone_number in body['phone_number']
    assert profile.address in body['address']
    assert profile.location in body['location']
    assert str(profile.birth_date) in body['birth_date']

    profile.delete()
    user.delete()

  def test_create_profile_info(self):
    user = User.objects.create()
    body = {
      'phone_number': '666666666', 
      'address': 'fake street 123', 
      'location': 'somewhere', 
      'birth_date': '2023-04-23', 
    }

    assert hasattr(user, 'profile') == False

    self.client.force_login(user=user)
    self.client.post(self.profile_edit_url, body)

    user.refresh_from_db()
    assert hasattr(user, 'profile') == True
    assert user.profile.phone_number in body['phone_number']
    assert user.profile.address in body['address']
    assert user.profile.location in body['location']
    assert str(user.profile.birth_date) in body['birth_date']

    user.profile.delete()
    user.delete()

@pytest.mark.django_db
class TestDeleteProfile(TestCase):
  profile_delete_url = reverse('profile_delete')

  def test_update_profile_info(self):
    user = User.objects.create()
    profile = Profile.objects.create(user=user)

    assert hasattr(user, 'profile') == True

    self.client.force_login(user=user)
    self.client.post(self.profile_delete_url)

    user.refresh_from_db()
    assert hasattr(user, 'profile') == False

    user.delete()
