from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    username = forms.CharField(required=True, max_length=30, label='Логин', min_length=2)
    password1 = forms.CharField(required=True, max_length=30, label='Пароль', min_length=8)
    password2 = forms.CharField(required=True, max_length=30, label='Повторите пароль', min_length=8)
    firstname = forms.CharField(required=True, max_length=25, label='Номер телефона', min_length=10)

    error_messages = {
        'password_mismatch': "Пароли не совпадают.",
        'error': "Форма не валидна.",
        'username_exists': "Пользователь с таким именем уже существует.",
    }

    class Meta:
        model = User
        fields = (
            'username',
            'firstname',
            'email',
            'password1',
            'password2'
       )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User._default_manager.get(username=username)
            # if the user exists, then let's raise an error message
            raise forms.ValidationError(
                self.error_messages['username_exists'],  # my error message
                code='username_exists',  # set the error message key
            )
        except User.DoesNotExist:
            return username  # if user does not exist so we can continue the registration process

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstname']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user
