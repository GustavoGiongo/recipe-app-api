
from django.test import TestCase # type: ignore
from django.contrib.auth import get_user_model # type: ignore

class ModelTest(TestCase):
    def test_create_user_with_email_sucessful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))