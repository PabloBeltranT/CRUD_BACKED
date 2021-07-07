from rest_framework import serializers
from apps.mini_super_app.models import miniSuperModel

class miniSuperSerializer(serializers.ModelSerializer):
    ''' Serializador para objetos del modelo miniSuperModel '''

    class Meta:
         model = miniSuperModel # Tomamos como modelo miniSuperModel que contiene los usuarios registrados.
         fields = '__all__'     # Indicamos que deseamos serializar todos campos o columnas del modelo.