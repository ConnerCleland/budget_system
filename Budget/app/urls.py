from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'), 
    path('registration/', registration, name='registration'),
    path('admin/', admin.site.urls),
]
