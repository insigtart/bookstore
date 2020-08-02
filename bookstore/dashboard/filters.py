from .models import *
import django_filters

import crispy_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder, Fieldset, MultiField, Div, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, FieldWithButtons, StrictButton

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [ "title", "author", "languages" ,"topics","description" ]
        filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
         }
        


class BookFilterFormHelper(crispy_forms.helper.FormHelper):
    form_method = 'GET'
    layout =Layout(
        Div('title', style="background: rgb(193, 224, 241); border-radius:16px;margin: 8px", title="Căutare după o parte din titlul cărții", css_class="bigdivs"),
        Field('description', style='background: rgb(193, 224, 241);max-width: 8em'),
        FieldWithButtons('author', StrictButton("Go! găsește autorul și citește ce a scris...")),
        ButtonHolder(
            Submit('submit', 'Căutare după filtre', css_class='button white')
        ),       
        
    )
    AppendedText('title', 'appended text to show')