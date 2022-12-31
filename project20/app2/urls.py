from django.urls import path
from app2.views import *
app_name='AA'

urlpatterns=[
    path('puspha/',puspha,name='pushpa'),
    path('meghana/',meghana,name='meghana'),
]
