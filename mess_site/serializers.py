from rest_framework import serializers
from .models import MessExtras,MessMain,ExtrasOrder

#All existing models have been serialized
class MessMainSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MessMain
        fields = '__all__'

class MessExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MessExtras
        fields = '__all__'

class ExtrasOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtrasOrder
        fields = '__all__'