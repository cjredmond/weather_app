from django import forms
from .models import Top, Bottom, Shoes

import itertools

class TopForm(forms.ModelForm):
    class Meta:
        model = Top
        exclude = ('checkin',)

class BottomForm(forms.ModelForm):
    class Meta:
        model = Bottom
        exclude = ('checkin',)

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        exclude = ('checkin',)

class ActualForm(forms.Form):
    parent_forms = [TopForm, BottomForm, ShoesForm]
    def __init__(self, parent_forms=[], *args, **kwargs):
        super(ActualForm,self).__init__(*args, **kwargs)

        parent_forms = parent_forms if parent_forms else self.parent_forms

        form_values = list(itertools.chain(
            *[form().fields.iteritems() for form in parent_forms]
        ))

        for k, v in form_values:
            self.fields[k] = v
