from django.forms import ModelForm
from .models import Trasacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Trasacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
