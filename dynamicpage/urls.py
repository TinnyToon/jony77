from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datacreate/', views.create_data, name='create_data'),
    path('dataview/', views.view_data, name='view_data'),
]
