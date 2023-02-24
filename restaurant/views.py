from django.shortcuts import render

from restaurant.serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

from rest_framework.generics import RetrieveUpdateAPIView,DestroyAPIView,ListCreateAPIView

from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer

    
    
    





