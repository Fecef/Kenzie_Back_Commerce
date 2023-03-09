from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isVendor, CustomPermission


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isVendor]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class OneProductView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'prod_id'


class ListProductsView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        varURL = self.kwargs['varURL']
        if varURL is not None:
            queryset_name = Product.objects.filter(name__icontains=varURL)
            if queryset_name:
                return queryset_name
            queryset_category = Product.objects.filter(category__icontains=varURL)
            if queryset_category:
                return queryset_category
