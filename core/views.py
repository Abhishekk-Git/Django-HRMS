from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView

from core.mixins import HRRequiredMixin


class BaseCreateView(
    HRRequiredMixin,
    CreateView,
):

    service = None

    def form_valid(self, form):

        self.object = self.service.create(form, request=self.request)

        return HttpResponseRedirect(
            self.get_success_url()
        )
        
        
from django.views.generic import UpdateView


class BaseUpdateView(
    HRRequiredMixin,
    UpdateView,
):

    service = None

    def form_valid(self, form):

        self.object = self.service.update(form)

        return HttpResponseRedirect(
            self.get_success_url()
        )
        
from django.views.generic import DeleteView


class BaseDeleteView(
    HRRequiredMixin,
    DeleteView,
):

    service = None

    def form_valid(self, form):

        self.service.delete(self.object)

        return HttpResponseRedirect(
            self.get_success_url()
        )