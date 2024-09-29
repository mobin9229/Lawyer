from rest_framework import viewsets
from .models import Product, Lawyer, ImageTitle, BackgroundImage
from .serializers import ProductSerializer, LawyerSerializer, ImageTitleSerializer, BackgroundImageSerializer


class BackgroundImageViewSet(viewsets.ModelViewSet):
    queryset = BackgroundImage.objects.all()
    serializer_class = BackgroundImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LawyerViewSet(viewsets.ModelViewSet):
    queryset = Lawyer.objects.all()
    serializer_class = LawyerSerializer

class ImageTitleViewSet(viewsets.ModelViewSet):
    queryset = ImageTitle.objects.all()
    serializer_class = ImageTitleSerializer