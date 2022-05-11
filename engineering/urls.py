from django.urls import path , include
from engineering.views.projectViews import Project , ProjectList
from . import views
urlpatterns = [

    path('project/<int:pk>/', Project.as_view()),
    path('project-list-create/', ProjectList.as_view() ),
    # path('customer/get-all/', views.CustomersView.as_view())

]