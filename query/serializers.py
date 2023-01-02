from rest_framework import serializers
from .models import QueryResponse, Query

#All existing models have been serialized

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Query
        fields = '__all__'

class QueryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model  = QueryResponse
        fields = '__all__'