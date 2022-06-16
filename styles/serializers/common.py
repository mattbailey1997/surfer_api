from rest_framework.serializers import ModelSerializer
from ..models import Style

class StyleSerializer(ModelSerializer):
  class Meta:
      model = Style
      fields = '__all__'