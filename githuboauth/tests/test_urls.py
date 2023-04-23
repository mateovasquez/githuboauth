from django.http import HttpResponse
import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestLoginRequired:
  home_url = reverse("home")
  profile_url = reverse("my_profile")

  def test_pages_access_logged_in(self, client):
    user = User.objects.create()
    client.force_login(user=user)

    response_home = client.get(self.home_url).content
    assert b'You are logged in' in response_home

    response_profile = client.get(self.profile_url).content
    assert b'This is my profile' in response_profile

    user.delete()

  def test_pages_access_logged_out(self, client):
    redirect_status_code = 302
    login_redirect_home_url = '/accounts/login/?next=/'
    login_redirect_profile_url = '/accounts/login/?next=/my-profile'

    response_home = client.get(self.home_url)
    assert response_home.url == login_redirect_home_url
    assert response_home.status_code == redirect_status_code

    response_profile = client.get(self.profile_url)

    assert response_profile.url == login_redirect_profile_url
    assert response_profile.status_code == redirect_status_code

@pytest.mark.django_db
class TestGetUserInfo:
  profile_url = reverse("my_profile")

  def test_user_info(self, client):
    user = User.objects.create(
      username="wolf&badger",
      first_name="wolf",
      last_name="badger"
    )
    client.force_login(user=user)
    response = client.get(self.profile_url)

    response_data = response.context['user_form'].__dict__['initial']
    assert response_data['username'] == user.username
    assert response_data['first_name'] == user.first_name
    assert response_data['last_name'] == user.last_name

    user.delete()
