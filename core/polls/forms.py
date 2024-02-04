from django import forms


class ResponseForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = question.choice_set.all()
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[(choice.id, choice.choice_text) for choice in choices],
                widget=forms.RadioSelect,
                required=True,
                label=question.question_text
            )