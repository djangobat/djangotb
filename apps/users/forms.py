from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import bootstrap
from crispy_forms.layout import Field
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username',)


class CustomCheckbox(Field):
    template = 'includes/custom_date.html'


class CustomUserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(label=_('Birth date'))
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email_field = bootstrap.PrependedText(
                                    "email",
                                    '<i class="fas fa-envelope"></i>',
                                    css_class="form-control",
                                    placeholder="contact@example.com")
        birth_date_field = bootstrap.PrependedText(
                                    "birth_date",
                                    '<i class="fa fa-calendar"></i>',
                                    css_class="datetimepicker")
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = "profile"
        self.helper.layout = Layout(
            'username',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column(email_field),
                Column(CustomCheckbox('birth_date')),
            ),
            Submit('submit', _('Update')),
        )