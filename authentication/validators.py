
import re


from django.core.exceptions import ValidationError
from django import forms


class NumericValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise forms.ValidationError(
                ("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise forms.ValidationError(
                ("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 uppercase letter, A-Z."
        )

class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise forms.ValidationError(
                ("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least 1 lowercase letter, a-z."
        )

class CharacterValidator:
    def validate(self, password, user=None):
        print("hnojk,i")
        # for character in password:
        #     if character in emoji_class.un
        #         raise forms.ValidationError(
        #             _("The password must not contain emoji."),
        #
        #         )


    def get_help_text(self):
        return 'Your password can not contain emoji.'
