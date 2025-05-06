from rest_framework.serializers import ModelSerializer, StringRelatedField
from core.models import Veiculo, Acessorio, Cor, Modelo
 
class VeiculoSerializer(ModelSerializer):
 
     class Meta:
         model = Veiculo
         fields = ('id', 'modelo', 'cor', 'ano', 'preco', 'acessorios')
         read_only_fields = ('id',)