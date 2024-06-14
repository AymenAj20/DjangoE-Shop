from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


#Pour convertire les objs de type Product en JSON 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # touts les champs 

