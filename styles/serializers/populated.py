from .common import StyleSerializer
from surfers.serializers.common import SurferSerializer

class PopulateStyleSerializer(StyleSerializer):
    surfers = SurferSerializer (many=True)