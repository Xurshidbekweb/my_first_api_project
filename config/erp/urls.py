from django.urls import path
from .views import IndexApiView

urlpatterns = [
    path('',IndexApiView.as_view(),name="index")
]
