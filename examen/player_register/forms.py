from django import forms
from .models import Player
from .models import Team
from .models import Stadium
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields ='__all__'

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields ='__all__'


