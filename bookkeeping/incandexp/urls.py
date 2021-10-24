from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="incandexp"),
    path('add-expense', views.add_expense, name="add-expense")
]