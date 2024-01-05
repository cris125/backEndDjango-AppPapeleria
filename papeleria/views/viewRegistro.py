from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from ..models.registros import Registros
from ..serializers.registroSerializers import RegistroSerializers
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
"""from rest_framework.permissions import IsAuthenticated"""
class ViewRegistro(views.APIView):
    queryset = Registros.objects.all()
    serializer_class = RegistroSerializers
    """permission_classes = (IsAuthenticated,)"""
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        
        serializer = RegistroSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()          
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
    
    def put(self, request, *args, **kwargs):
        try:
            registro_instance = Registros.objects.get(pk=kwargs['pk'])
            
        except Registros.DoesNotExist:
            return Response(
                {"res": "Object with specified ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RegistroSerializers(instance=registro_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            registro_instance = Registros.objects.get(pk=kwargs['pk'])
        except Registros.DoesNotExist:
            return Response(
                {"res": "Object with specified ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registro_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
            )