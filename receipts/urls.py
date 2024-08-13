from django.urls import path
from receipts.views import Home

urlpatterns = [
    path("", Home, name="Home"),
]
