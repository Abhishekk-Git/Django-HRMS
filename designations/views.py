from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Q

from core.mixins import BaseLoginMixin
from core.views import BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import Designation
from .services import DesignationService
from .forms import DesignationForm



class DesignationListView(
    BaseLoginMixin,
    ListView,
):

    model = Designation

    template_name = "designations/designation_list.html"

    context_object_name = "designations"

    paginate_by = 10
        
    def get_queryset(self):

        queryset = Designation.objects.filter(is_active=True).select_related("department")

        search = self.request.GET.get("search")

        if search:

            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        return queryset.order_by("title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        return context
        

class DesignationCreateView(BaseCreateView):

    service = DesignationService
    template_name = "designations/designation_form.html"
    form_class = DesignationForm
    success_url = reverse_lazy("designation_list")
    
    
class DesignationUpdateView(BaseUpdateView):

    model = Designation
    form_class = DesignationForm
    service = DesignationService
    template_name = "designations/designation_form.html"

    success_url = reverse_lazy("designation_list")
    
    
class DesignationDeleteView(BaseDeleteView):

    model = Designation
    template_name = "designations/designation_confirm_delete.html"
    context_object_name = "designation"
