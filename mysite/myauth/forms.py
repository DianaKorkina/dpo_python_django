from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "user", "avatar"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )