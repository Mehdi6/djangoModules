from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Category, Product, ProductMedia, Brand, Review
# Create your views here.

class StoreView(ListView):
    model = Product
    template_name = 'store/store.html'
    filter_context = {'query':'', 'category':'', 'minPrice':'', 'maxPrice':''}
    
    def get_queryset(self):
        queryset = super(StoreView, self).get_queryset()

        q = self.request.GET.get("q")
        minPrice = self.request.GET.get("minPrice")
        maxPrice = self.request.GET.get("maxPrice")
        
        if q:
            queryset = queryset.filter(name__icontains = q)
            self.filter_context['query'] = q
        
        if 'category' in self.kwargs and len(self.kwargs['category']) > 0:
            cat = Category.objects.filter(slug = self.kwargs['category'])
            sub_cat = Category.objects.filter(parent_cat__in=cat)
            queryset = queryset.filter(category__in= cat|sub_cat)
            self.filter_context['category'] = self.kwargs['category']
        
        if minPrice:
            queryset = queryset.filter(price__gte=minPrice)
            self.filter_context['minPrice'] = minPrice
            
        if maxPrice:
            queryset = queryset.filter(price__lte=maxPrice)
            self.filter_context['maxPrice'] = maxPrice
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['list_product'] = []
        #product_medias = ProductMedia.objects.filter(product_id in [prod.id for prod in context['product_list']]).filter(isPrimary=True)
        for i in range(len(context['product_list'])):
            
            pm = ProductMedia.objects.get(product_id=context['product_list'][i].id, isPrimary=True)
            context['list_product'].append({'product': context['product_list'][i], 'media': pm})
        
        context['product_list'] = ''
        context.update(self.filter_context)
        
        return context
        
class AjaxStoreView(View):
    pass