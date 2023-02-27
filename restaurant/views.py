from django.shortcuts import render
from requests import Response

from restaurant.serializers import BookingSerializer, MenuSerializer
from .models import Booking, Menu

from rest_framework.generics import RetrieveUpdateAPIView,DestroyAPIView,ListCreateAPIView

from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

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
    permission_classes = [IsAuthenticated]

    
    
    





