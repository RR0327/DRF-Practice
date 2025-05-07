# apis/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field
from django.core.exceptions import PermissionDenied

class NoNewUsersUntilEmailConfirmedAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

    def login(self, request, user):
        if not user.emailaddress_set.filter(verified=True).exists():
            raise PermissionDenied("Please verify your email before logging in.")
        return super().login(request, user)
