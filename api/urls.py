from django.urls import path
from .views import RabbitGetCreate, RabbitGetDelete

urlpatterns = [
    path('',RabbitGetCreate.as_view ),
    path('<int:pk>',RabbitGetDelete.as_view())

]
