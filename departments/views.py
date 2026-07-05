from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q

from core.mixins import HRRequiredMixin, BaseLoginMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Department
from .forms import DepartmentForm
from .services import DepartmentService


class DepartmentListView(BaseLoginMixin, ListView):

    model = Department

    paginate_by = 10

    template_name = "department/department_list.html"

    context_object_name = "departments"

    # def get_queryset(self):

    #     return Department.objects.filter(
    #         is_active=True
    #     )
        
    def get_queryset(self):

        queryset = Department.objects.filter(
            is_active=True
        )

        search = self.request.GET.get("search")

        if search:

            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )

        return queryset.order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        return context

class DepartmentCreateView(
    BaseLoginMixin,
    CreateView,
):

    form_class = DepartmentForm

    template_name = "department/department_form.html"

    success_url = reverse_lazy(
        "department_list"
    )
    
    def form_valid(self, form):

        self.object = DepartmentService.create_department(form)
        messages.success(self.request, f"Department {self.object.name} created successfully.")

        return HttpResponseRedirect(
            self.get_success_url()
        )
        
class DepartmentDetailView(BaseLoginMixin, DetailView):
    model = Department
    template_name = 'department/department_details.html'
    context_object_name = 'department'
    
    def get_queryset(self):
        return Department.objects.filter(is_active=True)
 
class DepartmentUpdateView(HRRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/department_form.html"
    success_url = reverse_lazy("department_list")
    
    
class DepartmentDeleteView(HRRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Department
    template_name = "department/department_confirm_delete.html"
    permission_required = "departments.deactivate_department"
    success_url = reverse_lazy("department_list")

    def form_valid(self, form):

        DepartmentService.deactivate_department(self.object)

        return HttpResponseRedirect(self.get_success_url())
