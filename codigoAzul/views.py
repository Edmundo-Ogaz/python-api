from codigoAzul.models import Albergue
from codigoAzul.serializers import AlbergueSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def albergue_list(request, format=None):
    if request.method == 'GET':
        albergues = Albergue.objects.all()
        serializer = AlbergueSerializer(albergues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbergueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)