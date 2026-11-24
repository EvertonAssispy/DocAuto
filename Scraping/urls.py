from django.urls import path
from .Views import ExplorarRepositorioView

urlpatterns = [
    path("explorar/", ExplorarRepositorioView.as_view(), name="explorar-repositorio"),
]