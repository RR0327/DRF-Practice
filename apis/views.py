from rest_framework import viewsets
from .models import RRModel
from .serializers import RRModelSerializer

# API ViewSet for RRModel
class RRModelViewSet(viewsets.ModelViewSet):
    queryset = RRModel.objects.all()
    serializer_class = RRModelSerializer
