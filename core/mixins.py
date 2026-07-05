from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class BaseLoginMixin(LoginRequiredMixin):

    login_url = "login"


class HRRequiredMixin(BaseLoginMixin):

    # def dispatch(self, request, *args, **kwargs):

    #     if not request.user.is_hr:
    #         raise PermissionDenied()

    #     return super().dispatch(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_hr:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied