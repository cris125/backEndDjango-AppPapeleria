from rest_framework import status, views
from rest_framework.response import Response
from ..models.registros import Registros
from ..serializers.registroSerializers import RegistroSerializers


class ViewRegistroNoAut(views.APIView):
    queryset = Registros.objects.all()
    serializer_class = RegistroSerializers

    def get_object(self, pk):
        try:
            return Registros.objects.get(pk=pk)
        except Registros.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:

            registro_instance = self.get_object(pk)
            if registro_instance:
                serializer = RegistroSerializers(registro_instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"res": "Object with specified ID does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            branchs = Registros.objects.all()
            serializer = RegistroSerializers(branchs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    