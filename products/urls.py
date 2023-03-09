from django.urls import path
from .views import ProductView, OneProductView, ListProductsView

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('product/<str:prod_id>/', OneProductView.as_view()),
    path('products/<str:varURL>/', ListProductsView.as_view()),
]
