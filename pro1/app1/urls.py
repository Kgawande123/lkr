from django.urls import  path
from .views import *
urlpatterns = [
    path("hv/",hview),
    path("pv/",pview),
    path("sv/",sview),
    path("uv/<int:pk>/",uview),
    path("dv/<int:k>/",dview),

]