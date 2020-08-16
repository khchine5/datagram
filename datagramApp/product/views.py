from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import NameFilter


from .models import Chain, Product, Store
from .serializers import ChainSerializer, ProductSerializer, StoreSerializer


class ChainViewSet(viewsets.ModelViewSet):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NameFilter

    @action(detail=True, methods=['get'])
    def do_scrap_website(self, request, pk=None):
        chain = self.get_object()
        #chain.do_scrap_products()
        #serializer = ChainSerializer(data=request.data)
        if True:
            count = chain.do_scrap_products()
            return Response({'count':str(count) })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NameFilter

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NameFilter
