from rest_framework import serializers
from .models import Query

#All existing models have been serialized
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Query
        fields = '__all__'