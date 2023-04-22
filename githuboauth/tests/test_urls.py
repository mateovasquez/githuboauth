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

    response_home = client.get(self.home_url)
    assert response_home.status_code == redirect_status_code

    response_profile = client.get(self.home_url)
    assert response_profile.status_code == redirect_status_code
