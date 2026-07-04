from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm
from .services import AuthenticationService


class LoginView(View):

    template_name = "accounts/login.html"

    def get(self, request):

        form = LoginForm()

        return render(
            request,
            self.template_name,
            {
                "form": form
            }
        )

    def post(self, request):

        form = LoginForm(request.POST)

        if not form.is_valid():

            return render(
                request,
                self.template_name,
                {
                    "form": form
                }
            )

        username = form.cleaned_data["username"]

        password = form.cleaned_data["password"]

        user = AuthenticationService.authenticate_user(
            username,
            password,
        )

        if user:

            login(request, user)

            messages.success(
                request,
                f"Welcome {user.first_name}"
            )

            return redirect("employee_list")

        messages.error(
            request,
            "Invalid username or password."
        )

        return render(
            request,
            self.template_name,
            {
                "form": form
            }
        )
        
    def dispatch(self, request, *args, **kwargs):

            if request.user.is_authenticated:

                return redirect("employee_list")

            return super().dispatch(
                request,
                *args,
                **kwargs
            )
        

class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect("login")