
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.name_views,name="namei"),
    path("surname_view",views.surname_view,name="surname_view"),
    path("city_view",views.city_view,name="city_view"),
    path("result_view",views.result_view,name="result_view")
]
