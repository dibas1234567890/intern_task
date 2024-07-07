from django.forms import ModelForm
from poll.models import pollModel

class pollForm(ModelForm):

    class Meta: 
        fields = "__all__"
        model = pollModel