from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ApplyForm

# Create your views here.


def index(request):
    return render(request, "forms/index.html")


class ApllyFormView(FormView):
    template_name = "forms/apply_form.html"
    form_class = ApplyForm
    success_url = reverse_lazy("result")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ApllyResultView(TemplateView):
    template_name = "forms/apply_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sucess"] = "succeed"
        return context
