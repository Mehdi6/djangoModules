from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Testimonial
from .forms import ContactForm
from .mixins import AjaxFormMixin

# Create your views here.

class HomeView(AjaxFormMixin, FormView):
    template_name = 'pages/home.html'
    form_class = ContactForm
    #success_url = None
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonial_list'] = Testimonial.objects.all()
        return context