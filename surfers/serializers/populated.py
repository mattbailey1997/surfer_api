from .common import SurferSerializer
from reviews.serializers.common import ReviewSerializer
from styles.serializers.common import StyleSerializer

class PopulatedSurferSerializer(SurferSerializer):

    reviews = ReviewSerializer(many=True)
    styles = StyleSerializer(many=True)