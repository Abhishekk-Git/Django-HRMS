from django.views.generic import TemplateView

from core.mixins import BaseLoginMixin
from dashboard.services import DashboardService


class DashboardView(BaseLoginMixin, TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
            
        context.update(
            DashboardService.get_statistics(user)
        )

        return context
