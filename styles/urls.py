from django.urls import path
from .views import StyleListView

urlpatterns = [
    path('', StyleListView.as_view())
]