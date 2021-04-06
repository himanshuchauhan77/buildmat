from django.test import TestCase
from ..models import PhoneModel
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def tests_create_user(self):
        """Test Creating a new user with email is successful"""
        phone_no = PhoneModel.objects.create(mobile=70565)
        User = get_user_model()
        user = User.objects.create_user(email='himanshu.chauhan95@gmail.com',
                                        phone_no=phone_no, password='foo')
        self.assertEqual(user.email,
                         'himanshu.chauhan95@gmail.com')
        self.assertTrue(user.check_password('foo'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        # try:
        #     self.assertEqual(user.username,'')
        # except AttributeError:
        #     pass
        # with self.assertRaises(TypeError):
        #     User.objects.create_user()
        # with self.assertRaises(TypeError):
        #     User.objects.create_user(email='')
        # with self.assertRaises(ValueError):
        #     User.objects.create_user(email='', password="foo")
