import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestLoginRequired:
  home_url = reverse("home")
  profile_url = reverse("my_profile")

  def test_home_access_logged_in(self, client):
    user = User.objects.create()
    client.force_login(user=user)
    response_content = client.get(self.home_url).content

    assert b'You are logged in' in response_content

    user.delete()

  def test_home_access_logged_out(self, client):
    response = client.get(self.home_url)
    redirect_status_code = 302

    assert response.status_code == redirect_status_code

  def test_profile_access_logged_in(self, client):
    user = User.objects.create()
    client.force_login(user=user)
    response_content = client.get(self.profile_url).content

    assert b'This is my profile' in response_content

    user.delete()

  def test_profile_access_logged_out(self, client):
    response = client.get(self.profile_url)
    redirect_status_code = 302
    
    assert response.status_code == redirect_status_code