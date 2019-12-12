""" User curate suggestions forms
"""
from django import forms


class DisambiguationForm(forms.Form):
    """
    Form to choose the correct name.
    """
    names = forms.ChoiceField(widget=forms.RadioSelect(), required=True)
    NAMES_OPTIONS = []

    def __init__(self, dict_names):
        self.NAMES_OPTIONS = []
        self.NAMES_OPTIONS.append(('', 'None'))

        for name in dict_names:
            self.NAMES_OPTIONS.append((str(dict_names[name]), str(name)))

        super(DisambiguationForm, self).__init__()
        self.fields['names'].choices = []
        self.fields['names'].choices = self.NAMES_OPTIONS
