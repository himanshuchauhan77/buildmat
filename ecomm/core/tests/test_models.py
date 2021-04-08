from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def tests_create_user(self):
        """Test Creating a new user with email is successful"""
        phone_no = 7056537787
        User = get_user_model()
        user = User.objects.create_user(email='himanshu.chauhan95@gmail.com',
                                        phone_no=phone_no,
                                        password='foo',
                                        phone_no_verified=False)
        self.assertEqual(user.email,
                         'himanshu.chauhan95@gmail.com')
        self.assertEqual(user.phone_no,
                         7056537787)
        self.assertTrue(user.check_password('foo'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
