from django import forms
from Account.models import *


class SignupForm(forms.ModelForm):
    """
    A Custom form for creating new users.
    """
    # password = forms.CharField(widget=forms.PasswordInput,label=("Password"))

    class Meta:
        # model = get_user_model()
        model = User
        fields = ['first_name','last_name','email','password']



    Widget  = {
        # 'password':forms
    }