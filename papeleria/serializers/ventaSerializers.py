from ..models.registros import Registros
from ..models.ventas import Ventas
from rest_framework import serializers

class  VentasSerializers(serializers.ModelSerializer):
   class Meta:
      
       model = Ventas
       fields = ['id', 'dateTime', 'nameProduct','valueProduct','registro'] 

def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'dateTime': instance.dateTime,
            'value':instance.value,
            'nameProduct':instance.nameProduct,
            'valueProduct': instance.valueProduct,
            'registro': instance.registro_id,
        }

        return representation