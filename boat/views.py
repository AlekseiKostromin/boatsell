from django.urls import path
from django.views.generic import ListView

from boat.models import Boat


class BoatListView(ListView):
    model = Boat


urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
]

