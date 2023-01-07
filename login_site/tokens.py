from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class TokenGenerator(PasswordResetTokenGenerator):
    def make_token(self,user,timestamp):
        return(
            six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()