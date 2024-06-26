from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30,label='Username')
    password=forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label='Password Confirm',widget=forms.PasswordInput)
    
    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        confirm=self.cleaned_data['confirm']
        if password and confirm and password!=confirm:
            raise forms.ValidationError('The passwords are not the same.')
        values={
            'username':username,
            'password':password
        }
        return values
    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,label='Username')
    password=forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput)