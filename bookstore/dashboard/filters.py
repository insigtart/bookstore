from .models import *
import django_filters

import crispy_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Fieldset


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [ "title", "author", "languages", "topics", "description", ]


class BookFilterFormHelper(crispy_forms.helper.FormHelper):
    form_method = 'GET'
    layout = Layout(
        Fieldset(
            'Filtrare -- în curs de realizare...',
            'title',
            'author',
            'languages',
            'topics',
            'description'
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )