from django.urls import path
#different things mind it while coding
from .views import *
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addsp/', views.add_sp, name="add_sp"),
    path('editsp/<int:id>', views.edit_sp, name="editsp"),
    path('deletesp/<int:id>', views.delete_sp, name="deletesp"),
]
