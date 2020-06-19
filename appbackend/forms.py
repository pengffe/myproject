from django import forms


class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=15, error_messages={
        'required': 'Password cannot be blank',
        'min_length': 'Password cannot be less 6 digits',
        'max_length': 'Password cannot be more than 15 digits'
    })
