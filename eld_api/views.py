from rest_framework import generics
from .models import DriverInfo
from .serializers import DriverInfoSerializer

class DriverInfoCreateView(generics.CreateAPIView):
    queryset = DriverInfo.objects.all()
    serializer_class = DriverInfoSerializer

    def perform_create(self, serializer):
        print("📥 Received data:", self.request.data)
        serializer.save()