from rest_framework import serializers
from .models import Product
from .models import Lawyer, ImageTitle, BackgroundImage


class BackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'

class ImageTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTitle
        fields = ['id', 'title', 'image']