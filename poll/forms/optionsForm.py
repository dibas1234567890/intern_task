from django.forms import ModelForm
from poll.models import Choice, Poll

class optionForm(ModelForm):

    class Meta: 
        fields = ['choice_text', 'poll']
        model = Choice
