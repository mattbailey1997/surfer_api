from django.urls import path #path allows us to set the url pattern with an endpoint
from .views import SurferDetailView, SurferListView

# Any request getting to this pount is prefixed with the /surfers/ endpount

# example: http://localhost:8000/surfer/

urlpatterns = [
  path('', SurferListView.as_view()), #as_view passes the httprequest onto the attribute on the view
  path('<int:pk>/', SurferDetailView.as_view())
]