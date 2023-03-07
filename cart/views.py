from django.shortcuts import render
from rest_framework import generics


class CartView(generics.ListCreateAPIView):
    ...
