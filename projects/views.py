from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q

from core.mixins import BaseLoginMixin, HRRequiredMixin
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Project
from .service import ProjectService
from .forms import ProjectForm


class ProjectListView(
    BaseLoginMixin,
    ListView,
):

    model = Project

    template_name = "projects/project_list.html"

    context_object_name = "projects"

    paginate_by = 10
        
    def get_queryset(self):

        queryset = Project.objects.filter(
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
        

class ProjectCreateView(BaseCreateView):

    service = ProjectService
    template_name = "projects/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("project_list")
    
    
class ProjectUpdateView(BaseUpdateView):

    model = Project
    form_class = ProjectForm
    service = ProjectService
    template_name = "projects/project_form.html"

    success_url = reverse_lazy("project_list")
    
    
class ProjectDetailView(
    HRRequiredMixin,
    DetailView,
):

    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    def get_queryset(self):
        return Project.objects.filter(is_active=True)
