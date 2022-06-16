# rest_framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


# custom imports
from .models import Surfer
from .serializers.common import SurferSerializer
from .serializers.populated import PopulatedSurferSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SurferListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    # in this controller, we just want to get all the items inside the albums table and return it as a response

    # Endpints and Methods
    #  GET SURFERS /surfers/
    # POST /sufers/

    # SUrfers
    def get(self, _request):

        surfers = Surfer.objects.all()  # get all fields using all() method
        # .all() returns a QuerySet, we need to use the serializer to convert this into a python datatype

        # Need to do many = true if we expect multiple items in the QuerySet
        serialized_surfers = SurferSerializer(surfers, many=True)
        print('serialized data ->', serialized_surfers.data)
        return Response(serialized_surfers.data, status.HTTP_200_OK)

# POST
    def post(self, request):
        # print('Request', request.data)
        deserialized_surfer = SurferSerializer(data=request.data)

        try:
            deserialized_surfer.is_valid()

            deserialized_surfer.save()

            return Response(deserialized_surfer.data, status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({'detail': str(e)}, status.HTTP_422_UNPROCESSABLE_ENTITY)



# Endpoint is anything that is going to have our PK on it
class SurferDetailView(APIView):
    # Get one

    def get_surfer(self, pk):
      try:
            
          return Surfer.objects.get(pk=pk)
      except Surfer.DoesNotExist as e:
          print(e)
          raise NotFound({ 'detail': str(e) }, status.HTTP_404_NOT_FOUND)
      
      
    def get(self, _request, pk):
      surfer = self.get_surfer(pk)
      print('surfer --->', surfer)
      serialized_surfer = PopulatedSurferSerializer(surfer)
      return Response(serialized_surfer.data, status.HTTP_200_OK)


  #Delete
    def delete(self, _request, pk):
      surfer_to_delete = self.get_surfer(pk)
      surfer_to_delete.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


  #Update This function
    def put(self, request, pk):
      surfer_update = self.get_surfer(pk)
      deserialized_surfer = SurferSerializer(instance=surfer_update, data=request.data)

      try:
        deserialized_surfer.is_valid()
        deserialized_surfer.save()

        return Response(deserialized_surfer.data, status.HTTP_202_ACCEPTED)

      except Exception as e:
        print(e)
        return Response({ 'detail': str(e) }, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
