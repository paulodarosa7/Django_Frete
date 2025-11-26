from django import forms

from .models import Usuario, Freteiro, solicitarFrete, Rota

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
    
class FreteForm(forms.ModelForm):
    class Meta:
        model = solicitarFrete
        fields = ['produto', 'peso', 'largura', 'altura', 'valor', 'endereco_coleta', 'endereco_entrega']
        widgets = {
            'produto': forms.Textarea(attrs={'rows': 2}),
            'endereco_coleta': forms.Textarea(attrs={'rows': 2}),
            'endereco_entrega': forms.Textarea(attrs={'rows': 2})
        }

class RotaForm(forms.ModelForm):
    class Meta:
        model = Rota
        fields = ['origem', 'destino', 'distancia', 'custo', 'tempo_minutos']
        widgets = {
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'distancia': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'custo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tempo_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
        }