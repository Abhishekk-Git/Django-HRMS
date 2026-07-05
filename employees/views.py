from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from core.mixins import HRRequiredMixin, BaseLoginMixin

from .models import Employee
from .forms import EmployeeCreateForm, EmployeeUpdateForm
from .services import EmployeeService

User = get_user_model()

class EmployeeListView(BaseLoginMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 2  # Number of employees per page
    
    # queryset = Employee.objects.select_related('user', 'department', 'designation').order_by("-employee_code")
    
    def get_queryset(self):

        queryset = Employee.objects.select_related(
            "user",
            "department",
            "designation",
        ).filter(
            is_active=True,
        )

        search = self.request.GET.get("search")

        if search:

            queryset = queryset.filter(
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) |
                Q(user__username__icontains=search) |
                Q(employee_code__icontains=search)
            )

        return queryset.order_by("employee_code")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        return context
    
    
class EmployeeCreateView(HRRequiredMixin, CreateView):
    model = Employee
    template_name = 'employees/employee_form.html'
    form_class = EmployeeCreateForm
    success_url = reverse_lazy('employee_list')  # Redirect to employee list after successful creation
    
    def form_valid(self, form):

        self.object = EmployeeService.create_employee(form)
        messages.success(self.request, f"Employee {self.object.user.get_full_name()} created successfully.")

        return HttpResponseRedirect(
            self.get_success_url()
        )
    
class EmployeeDetailView(BaseLoginMixin ,DetailView):
    model = Employee
    template_name = 'employees/employee_details.html'
    context_object_name = 'employee'
    
    def get_queryset(self):
        return Employee.objects.select_related('user', 'department', 'designation').filter(is_active=True)
    
    
class EmployeeUpdateView(HRRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")
    
    
class EmployeeDeleteView(HRRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    permission_required = "employees.delete_employee"
    success_url = reverse_lazy("employee_list")

    def form_valid(self, form):

        EmployeeService.delete_employee(self.object)

        return HttpResponseRedirect(self.get_success_url())
