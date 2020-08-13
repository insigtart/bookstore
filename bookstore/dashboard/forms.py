from django.forms import ModelForm
from django import forms
from .models import Book
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'datetime',
                  'country', 'languages', 'topics', 'description']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titlu'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
        #     'datetime': forms.TextInput(attrs={'class': 'form-control form_datetime', 'placeholder': 'Data publicării'}),
        #     'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Țări'}),
        #     'languages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Limbi'}),
        #     'topics': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categorii'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalii'}),
        # }


class EditBookModelForm(BSModalModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'datetime',
                  'country', 'languages', 'topics', 'description']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titlu'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
        #     'datetime': forms.TextInput(attrs={'class': 'form-control form_datetime', 'placeholder': 'Data publicării'}),
        #     'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Țări'}),
        #     'languages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Limbi'}),
        #     'topics': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categorii'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalii'}),
        # }
