from django import forms
from django.forms import ModelForm

from mainapp.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'surname', 'age', 'gender', 'departament', 'programming_language')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'id': 'acInput'
        })
        self.fields['departament'].empty_label = 'Выберите отдел'
        self.fields['programming_language'].empty_label = 'Выберите язык'
