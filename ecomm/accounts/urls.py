from django.urls import path
from accounts.views import CreateUserView

app_name = 'accounts'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
]
