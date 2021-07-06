from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import miniSuperSerializer
from apps.mini_super_app.models import miniSuperModel

@api_view(['GET', 'POST'])
def mini_super(request):
    ''' Retorna una lista de objetos serializados en caso de que el metodo del request sea GET y registra un nuevo usuario si el metodo es POST '''

    if request.method == 'GET':

        model_required = miniSuperModel.objects.all()
        model_required_serialized = miniSuperSerializer(model_required, many=True)
        return Response(model_required_serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        new_user = miniSuperSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response(data=new_user.data, status=status.HTTP_201_CREATED)
        return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mini_super_detail(request, pk):
    ''' Si la url contiene un identificador y el metodo de request sea GET retorna el objeto serializado que coincide con el identificador, si el metodo es PUT deserailiza la data en request y actauliza el objeto coicidente con el identificador, si el metodo es DELETE eleimina directamente el objeto encontrado coincidente con el identificador. '''

    try:
        model_required = miniSuperModel.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        model_required_serialized = miniSuperSerializer(model_required, many=False)
        return Response(model_required_serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        model_to_update = miniSuperSerializer(model_required, data=request.data)
        if model_to_update.is_valid():
            model_to_update.save()
            return Response(data=model_to_update.data, status=status.HTTP_200_OK)
        return Response(model_to_update.errors)

    elif request.method == 'DELETE':
        model_required.delete()
        return Response(status=status.HTTP_200_OK)