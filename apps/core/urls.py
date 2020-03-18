from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
]
