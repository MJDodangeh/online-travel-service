from django.urls import path
from .views import TripList

urlpatterns = [
      path('trip/search/', TripList.as_view()),
]