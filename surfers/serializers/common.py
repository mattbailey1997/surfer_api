from rest_framework import serializers #serializer holds our ModelSeriarlizer class
from ..models import Surfer # importing Album, but this time going up one level our albums foler using ..


class SurferSerializer(serializers.ModelSerializer):
    # define a Meta subclass that details which model and fields to serialize
    class Meta:
      model = Surfer #define model to serialize from
      fields = '__all__'
