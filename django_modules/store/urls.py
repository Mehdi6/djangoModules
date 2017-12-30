from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<category>[\w-]*)$',
        #view=views.HomeView.as_view(),
        #view=TemplateView.as_view(template_name='store/store.html'),
        view=views.StoreView.as_view(),
        name='store'
    ),
    url(
        regex=r'^$',
        #view=views.HomeView.as_view(),
        #view=TemplateView.as_view(template_name='store/store.html'),
        view=views.StoreView.as_view(),
        name='store'
    ),
    url(
        regex=r'^ajax/(?P<category>[\w-]*)$',
        #view=views.HomeView.as_view(),
        #view=TemplateView.as_view(template_name='store/store.html'),
        view=views.AjaxStoreView.as_view(),
        name='ajax-store'
    ),
]
