from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from address.views import AddressView, AddressUpdateView

from . import views

urlpatterns = [
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("user/", views.UserView.as_view()),
    path("user/address/", AddressView.as_view()),
    path("user/address/update/", AddressUpdateView.as_view()),
    path("user/<str:user_id>/", views.UserDetailView.as_view()),
    path("user/<str:user_id>/recover_account/", views.UserAccounRecoverView.as_view()),
]
