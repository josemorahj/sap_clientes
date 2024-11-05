from django.forms import ModelForm, EmailInput
from .models import Persona

class PersonaForm(ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
