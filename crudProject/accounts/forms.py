import re

from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_name = forms.CharField()
    email_id = forms.EmailField()
    contact_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput, label="Re Enter Password")



    def clean(self):
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['password']
        rpwd = total_cleaned_data['rpassword']
        if len(pwd) < 6:
            raise forms.ValidationError('password length should be 6')
        elif not re.search("[a-z]", pwd):
            raise forms.ValidationError('password should contain atleast one lowercase letter')
        elif not re.search("[0-9]", pwd):
            raise forms.ValidationError('password should contain atleast one digit letter')
        elif not re.search("[A-Z]", pwd):
            raise forms.ValidationError('password should contain atleast one Upper Case letter')
        elif not re.search("[_$#@!%&^*]", pwd):
            raise forms.ValidationError('password should contain atleast one Special Character')

        if pwd != rpwd:
            raise forms.ValidationError('password not matching')