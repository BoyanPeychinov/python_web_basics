from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            }
        )
    )