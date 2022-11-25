from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for k in self.fields.keys():
            self.fields[k].widget.attrs.update({'autocomplete': "off",
                                                'readonly': True,
                                                'onfocus': "this.removeAttribute('readonly')"})

        self.fields['username'].widget.attrs.update({'placeholder': "Username"})
        self.fields['password'].widget.attrs.update({'placeholder': "Password"})
        self.fields['repeat_password'].widget.attrs.update({'placeholder': "Repeat Password"})

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for k in self.fields.keys():
            self.fields[k].widget.attrs.update({'placeholder': k.capitalize()})

    class Meta:
        model = User
        fields = ['username', 'password']
