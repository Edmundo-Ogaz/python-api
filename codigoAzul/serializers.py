from codigoAzul.models import Albergue
from rest_framework import serializers

class AlbergueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albergue
        fields = ['id', 'region', 'tipo', 'comuna', 'nombre', 'direccion', 'institucion', 'horario', 'cupo', 'mapa']

# {
#     "region": "Arica y Parinacota", 
#     "tipo": "Albergue", 
#     "comuna": "Arica", 
#     "nombre": "Albergue", 
#     "direccion": "Tucapel 2518, Arica, Arica y Parinacota, Chile", 
#     "institucion": "Corporación Maymuru",
#     "horaio": "24 hrs.", 
#     "cupo": "20", 
#     "mapa": "pendienge"
# }