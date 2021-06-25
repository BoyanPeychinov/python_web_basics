from django import forms
from django.core.exceptions import ValidationError

from expenses_tracker.core.profile_utills import get_profile
from expenses_tracker.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    pass

