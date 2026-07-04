from django.urls import path
from .views import (EmployeeListView, EmployeeCreateView, EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView                )

urlpatterns = [
    # path('', views.employee_list, name='employee_list'),
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_details'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]


