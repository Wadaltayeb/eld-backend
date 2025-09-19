# from django.urls import path
# from django.urls import path
# from .views import DriverInfoCreateView

# urlpatterns = [
#     path('api/drivers/create/', DriverInfoCreateView.as_view(), name='create-driver-info'),
# ]


from django.urls import path
from .views import DriverInfoCreateView

urlpatterns = [
    path('drivers/create/', DriverInfoCreateView.as_view(), name='create-driver-info'),
]