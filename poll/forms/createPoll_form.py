from django.forms import ModelForm
from poll.models import Choice, Poll

class pollForm(ModelForm):

    class Meta: 
        fields = "__all__"
        model = Poll
