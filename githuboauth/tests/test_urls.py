import pytest
from django.urls import reverse
from django.test import TestCase

from django.contrib.auth.models import User

@pytest.mark.django_db
class TestLoginRequired(TestCase):
  private_urls = [
    reverse('home'),
    reverse('user_detail'),
    reverse('profile_detail'),
    reverse('profile_edit'),
    reverse('profile_delete'),
  ]

  def test_page_access_logged_in(self):
    user = User.objects.create()
    self.client.force_login(user=user)

    for url in self.private_urls:
      response = self.client.get(url)
      assert response.status_code == 200

    user.delete()

  def test_page_access_logged_out(self):
    redirect_status_code = 302

    for url in self.private_urls:
      redirect_url = f'/accounts/login/?next={url}'
      response = self.client.get(url)
      assert response.url == redirect_url
      assert response.status_code == redirect_status_code

