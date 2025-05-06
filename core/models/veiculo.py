from django.db import models
 
class Veiculo(models.Model):
     modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, related_name='veiculos')
     cor = models.ForeignKey('Cor', on_delete=models.CASCADE, related_name='veiculos')
     ano = models.IntegerField(blank=True, null=True, default=0)  
     preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)  
     acessorios = models.ManyToManyField('Acessorio', related_name='veiculos')  
 
     def __str__(self):
         return f"({self.id}) {self.modelo} - {self.cor} - {self.ano}"  