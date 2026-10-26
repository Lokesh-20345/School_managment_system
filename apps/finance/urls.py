from django.urls import path
from apps.finance import views
urlpatterns = [
    path('setfeestructure/',views.set_fee_structure),
    path('collectfee/',views.collect_fee),
    
]