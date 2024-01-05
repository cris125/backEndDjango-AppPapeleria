from ..models.registros import Registros
from rest_framework import serializers

class RegistroSerializers(serializers.ModelSerializer):
   class Meta:
       model = Registros
       fields = ['id', 'dateTime', 'name','value','existences','description', 'photoLink', 'user'] 

def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'dateTime': instance.dateTime,
            'value':instance.value,
            'existences':instance.existences,
            'name': instance.name,
            'description': instance.description,
            'photoLink':instance.photoLink,
            'user': instance.user_id,
            
        }

        
        return representation