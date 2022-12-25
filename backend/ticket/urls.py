from django.urls import path
from .views import TripList,TripBook,TravelsList,TripDetail

urlpatterns = [
      path('trip/search/', TripList.as_view()),
      path('trip/buy/', TripBook.as_view()),
      path('travels/', TravelsList.as_view()),
      path('trip/<int:pk>/', TripDetail.as_view()),
]