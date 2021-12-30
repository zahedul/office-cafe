from unittest.mock import patch
import pytest
from django.contrib.auth import get_user_model

from base_app import models


def sample_user(email='test@ifarmtech.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class TestModels:

    @pytest.mark.django_db
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        assert user.email == email
        assert user.check_password(password) is True

    @pytest.mark.django_db
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        assert user.email == email.lower()

    @pytest.mark.django_db
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with pytest.raises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    @pytest.mark.django_db
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@gmail.com',
            'test123'
        )

        assert user.is_superuser is True
        assert user.is_staff is True
