from django import forms
from poll.models import Choice

class VoteForm(forms.ModelForm):
   
    choice = forms.ModelMultipleChoiceField(queryset = Choice.objects.none(), 
                                            widget=forms.CheckboxSelectMultiple,
                                            )
    def __init__(self, poll, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(pk = poll.id)

    class Meta:
        model = Choice
        fields = ['choice']
