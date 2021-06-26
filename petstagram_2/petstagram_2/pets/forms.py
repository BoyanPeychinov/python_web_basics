from django import forms

from petstagram_2.core.forms import BootstrapFormMixin
from petstagram_2.pets.models import Pet


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2',
                }
            ),
            # 'age': forms.IntegerField(
            #     attrs={
            #         'type': 'number',
            #     }
            # ),
        }


class EditPetForm(CreatePetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
        }