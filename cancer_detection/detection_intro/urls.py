
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path('prediction/',views.prediction),
    path('predict/',views.predict)
]
