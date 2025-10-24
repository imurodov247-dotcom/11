from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('create/',views.create_xodim, name='create'),
    path('search/',views.search, name='search'),
    path('stat/',views.stat, name='stat'),
    
]
