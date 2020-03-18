from allauth.account.signals import password_changed
from django.utils.translation import ugettext as _
from django.dispatch import receiver
from django.contrib import messages


@receiver(password_changed)
def password_change_callback(sender, request, user, **kwargs):
    messages.success(request, _('You have Successfully changed your Password!.'), extra_tags="password_changed")