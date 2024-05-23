from django.urls import path
from .views import *
urlpatterns = [
    path('list',car_list_view,name="car_list"),
    path('<int:pk>',car_detail_view,name="car_detail")
]
