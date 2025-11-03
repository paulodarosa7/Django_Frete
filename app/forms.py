from django import forms

from .models import Usuario, Freteiro

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'tel', 'cpf', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
        
class FreteiroForm(forms.ModelForm):
    class Meta:
        model = Freteiro
        fields = ['nome', 'email', 'senha', 'tel', 'cpf', 'data_nascimento', 'cidade', 'estado']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
