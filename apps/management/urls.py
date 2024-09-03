from django.urls import path

from apps.management import views
from apps.management.views import EmployeeListView, EmployeeDeleteView, EmployeeUpdateView, EmployeeCreate

urlpatterns = [
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    path('', EmployeeCreate.as_view(), name='add_employee'),
    path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee_delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]