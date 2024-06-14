from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getRoute(request):
    return Response('Test API')


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serialized = ProductSerializer(products,many=True) # Pour rendre les données en Json many c pour dire il peut recevoire 0+ de objs
    return Response(serialized.data )

@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serialized = ProductSerializer(product,many=False)
    return Response(serialized.data)
