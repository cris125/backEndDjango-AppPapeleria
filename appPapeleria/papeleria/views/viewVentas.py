from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from ..models.ventas import Ventas
from ..serializers.ventaSerializers import VentasSerializers
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
"""from rest_framework.permissions import IsAuthenticated"""
class ViewVentas(views.APIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializers
    """permission_classes = (IsAuthenticated,)"""
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        
        serializer = VentasSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()          
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:

            ventas_instance = self.get_object(pk)
            if ventas_instance:
                serializer = VentasSerializers(ventas_instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"res": "Object with specified ID does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            branchs = Ventas.objects.all()
            serializer = VentasSerializers(branchs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    

    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            ventas_instance = Ventas.objects.get(pk=pk)
            ventas_instance.delete()
            return Response({"res": "Object deleted successfully"}, status=status.HTTP_200_OK)
        except KeyError:
            # No se proporcionó un pk, eliminar todos los objetos
            Ventas.objects.all().delete()
            return Response({"res": "All objects deleted successfully"}, status=status.HTTP_200_OK)
        except Ventas.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)