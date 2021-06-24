from django import forms
from django.forms import RadioSelect

from books_app.books.models import Book, Author


# class BookForm(forms.ModelForm):
#     author_name = forms.CharField(max_length=20)
#
#     def save(self, commit=True):
#         author = Author(
#             name=self.cleaned_data['author_name'],
#         )
#         author.save()
#         self.instance.author = author
#         return super().save(commit)
#
#     class Meta:
#         model = Book
#         fields = ['title', 'pages', 'description', 'author_name']


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class BookForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Book
        fields = ['title', 'pages', 'description']


class AuthorForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Author
        fields = '__all__'


class StateFilterForm(forms.Form):
    state = forms.ChoiceField(
        required=False,
        choices=(
            ('Done', 'done'),
            ('Not done', 'not done'),
            ('All', 'all'),
        )
    )
