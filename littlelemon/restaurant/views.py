from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuSerializer, UserSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    # POST, GET
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    # GET, PUT, DELETE
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


# check
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all() 
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    