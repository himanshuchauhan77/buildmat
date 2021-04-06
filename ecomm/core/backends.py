from django.db.models import Q
from django.contrib.auth import get_user_model
MyUser = get_user_model()


class EmailorPhoneBackend(object):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(Q(phone_no__mobile=username)
                                      | Q(email=username))
        except MyUser.DoesNotExist:
            return None
        return user if user.check_password(password) else None
