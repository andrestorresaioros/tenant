from django.urls import path
from a_home.views import *

urlpatterns = [
    path('', home_view, name="home"),  
    path('create_item/', create_item, name="create_item"),
]
