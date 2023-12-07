from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('predictImage', views.predict, name="predictImage")
]

