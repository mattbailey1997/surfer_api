from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers.populated import PopulateStyleSerializer
from .models import Style

# Create your views here.
class StyleListView(APIView):

  def get(self, _request):

    styles = Style.objects.all()
    serialized_styles = PopulateStyleSerializer(styles, many=True)
    return Response(serialized_styles.data)

