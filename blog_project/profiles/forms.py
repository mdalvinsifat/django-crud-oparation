from django import forms
from profiles.models import profile

class ProfileForm(forms.ModelForm):
    class Meta :
        model = profile
        fields = '__all__'