from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('name','email','portfolio','mobile')

        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.TextInput(attrs={"class":'form-control', 'placeholder':'Enter valid email'}),
            'portfolio' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'https://www.google.com'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter valid no'})
        }
