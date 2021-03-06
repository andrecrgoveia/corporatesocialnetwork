# Django's imports
from django.shortcuts import render

# Developer's imports
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Forms' imports
from .forms import CustomUserCreationForm


# This class makes a form to subscribed new users
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # This form is used to create new users
    template_name = "registration/signup.html"

    # This function redirect to login url when the new user is created
    def get_success_url(self):
        return reverse("login")


@login_required
def index(request):
    return render(request, "index.html")
