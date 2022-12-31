from django.urls import path
from app2.views import *
app_name='sonusood'

urlpatterns=[
    path('pasupathi/',pasupathi,name='pasupathi'),
]