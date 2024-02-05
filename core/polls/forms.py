from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ResponseForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = question.choice_set.all()
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[(choice.id, choice.text) for choice in choices],
                widget=forms.RadioSelect,
                required=True,
                label=question.text
            )
