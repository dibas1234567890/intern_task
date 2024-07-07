from django.forms import ModelForm
from poll.models import Choice, Poll

class Choices(ModelForm):

    class Meta: 
        fields = ['choice_text', 'poll']
        model = Choice
    def __init__(self, *args, **kwargs):
            poll_id = kwargs.pop('poll_id', None)
            super(Choices, self).__init__(*args, **kwargs)
            poll = Poll.objects.get(pk = poll_id)
            if poll:
                 self.poll = poll
                