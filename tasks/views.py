from django.views.generic import DetailView, ListView
from django.db.models import Q
from core.views import BaseCreateView, BaseDeleteView, BaseUpdateView
from tasks.choices import TaskStatus
from tasks.forms import TaskForm
from core.mixins import HRRequiredMixin, BaseLoginMixin
from tasks.models import Task
from .service import TaskService
from django.urls import reverse_lazy



class TaskListView(BaseLoginMixin,ListView,):

    model = Task
    paginate_by = 20
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    # def get_queryset(self):

    #     return (
    #         Task.objects
    #         .filter(is_active=True)
    #         .select_related(
    #             "project",
    #             "created_by",
    #         )
    #         .prefetch_related(
    #             "assigned_to",
    #         )
    #     )
    
        
    def get_queryset(self):

        queryset = (
            Task.objects
            .filter(is_active=True)
            .select_related(
                "project",
                "created_by"
            )
            .prefetch_related(
                "assigned_to"
            )
        )

        search = self.request.GET.get("search")

        if search:

            queryset = queryset.filter(
                Q(title__icontains=search)
                |
                Q(description__icontains=search)
            )
        status = self.request.GET.get("status")

        if status:

            queryset = queryset.filter(status=status)

        return queryset.order_by("due_date", "title")
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["status_choices"] = TaskStatus.choices
        context["search_query"] = self.request.GET.get("search", "")
        context["selected_status"] = self.request.GET.get("status", "")

        return context
    
class TaskCreateView(BaseCreateView):
    form_class = TaskForm
    service = TaskService
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(BaseUpdateView):
    model = Task
    form_class = TaskForm
    service = TaskService
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")
    
    
class TaskDetailView(HRRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        return (
            Task.objects
            .filter(is_active=True)
            .select_related("project", "created_by__user")
            .prefetch_related("assigned_to__user")
        )
    

class TaskDeleteView(BaseDeleteView):
    model = Task
    service = TaskService
    success_url = reverse_lazy("task_list")
    

class EmployeeTaskListView(BaseLoginMixin, ListView):

    model = Task
    template_name = "tasks/my_task.html"
    context_object_name = "tasks"
    paginate_by = 20

    def get_queryset(self):
        employee = getattr(self.request.user, "employee_profile", None)
        if employee is None:
            return Task.objects.none()

        queryset = (
            Task.objects
            .filter(
                assigned_to=employee,
                is_active=True
            )
            .select_related(
                "project"
            )
            .prefetch_related(
                "assigned_to__user"
            )
            .order_by("due_date", "title")
        )

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        status = self.request.GET.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_choices"] = TaskStatus.choices
        context["search_query"] = self.request.GET.get("search", "")
        context["selected_status"] = self.request.GET.get("status", "")
        return context
