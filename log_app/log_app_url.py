from django.urls import path 
from .views import ( 
    search_medicine_price,  
)

urlpatterns = [
    # path("preset/", include(crm_preset)),
    path('test/', search_medicine_price, name="search-medicine-api"),

]
