from django import forms
from django.forms import formset_factory


class DataCreationForm(forms.Form):
    name = forms.CharField(max_length=30)


DataNameSet = formset_factory(DataCreationForm, extra=0)
