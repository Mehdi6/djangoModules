from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.HomeView.as_view(),
        #view=TemplateView.as_view(template_name='pages/home.html'),
        name='home'
    ),
]
