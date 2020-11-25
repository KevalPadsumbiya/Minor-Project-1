from django import forms


class register_form(forms.Form):
    user_name = forms.CharField(max_length=20)
    user_email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())

class regi_succe(forms.Form):
    suc_user = forms.CharField(max_length=50)