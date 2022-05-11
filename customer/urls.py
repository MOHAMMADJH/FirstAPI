from django.contrib import admin
from django.urls import path , include
from .views import ping_pong , add_engineer
from . import views
urlpatterns = [
    path('' , ping_pong) ,
    path('ping-pong/' , ping_pong),
    path('add-engineer/' , add_engineer),
    path('details/<int:pk>/', views.CustomerDetails.as_view()),
    path('list/', views.CustomerList.as_view()),
    path('customer/get-all/', views.CustomersView.as_view()),






]
