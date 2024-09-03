from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.management.forms import EmployeeDetails
from apps.management.models import Employee


# Create your views here.

class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeDetails
    template_name = 'EmployeeForm.html'
    success_url = reverse_lazy('employee_list')

class EmployeeListView(ListView):
    model = Employee
    template_name = "employelist.html"
    context_object_name = "employees"


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'dob', 'department', 'phone_number', 'address', 'salary']
    template_name = 'employee_update.html'
    success_url = reverse_lazy('employee_list')

# Delete View


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')