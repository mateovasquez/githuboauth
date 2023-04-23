import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestLoginRequired:
  home_url = reverse('home')
  user_url = reverse('user_detail')

  def test_pages_access_logged_in(self, client):
    user = User.objects.create()
    client.force_login(user=user)

    response_home = client.get(self.home_url).content
    assert b'You are logged in' in response_home

    response_profile = client.get(self.user_url).content
    assert b'User Settings' in response_profile

    user.delete()

  def test_pages_access_logged_out(self, client):
    redirect_status_code = 302
    login_redirect_home_url = '/accounts/login/?next=/'
    login_redirect_user_url = '/accounts/login/?next=/user'

    response_home = client.get(self.home_url)
    assert response_home.url == login_redirect_home_url
    assert response_home.status_code == redirect_status_code

    response_profile = client.get(self.user_url)

    assert response_profile.url == login_redirect_user_url
    assert response_profile.status_code == redirect_status_code
