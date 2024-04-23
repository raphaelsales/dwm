from rest_framework import generics
from .models import Rabbit  
from .serializers import RabbitSerializer

class RabbitGetCreate(generics.ListCreateAPIView):
    queryset = Rabbit.objects.all()
    serializer_class = RabbitSerializer

class RabbitGetDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rabbit.objects.all()
    serializer_class = RabbitSerializer
