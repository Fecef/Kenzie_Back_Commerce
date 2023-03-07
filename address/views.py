from django.shortcuts import render
from rest_framework import generics


class AddressView(generics.ListCreateAPIView):
    ...
