from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Category, Product, ProductMedia, Brand, Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page

# Create your views here.

def extend_pagination(page, size_extension):
    remain_left = False
    remain_right = False
    range_extension = []
    
    len_paginator = page.paginator.num_pages
    current_page = page.number
        
    step_right = max(0, min(len_paginator - current_page, size_extension))
    step_left = min(size_extension*2 - step_right, current_page - 1)
    step_right += min(len_paginator - current_page - step_right, max(0, size_extension - step_left))
    
    if step_right == 0 and step_left == 0:
        return  {'remain_left':remain_left, 'remain_right':remain_right, 'ex_range': range_extension}
    
    if len_paginator - current_page > step_right:
        remain_right=True
    
    if current_page - size_extension > 1:
        remain_left = True
    
    for i in range(step_left):
        range_extension.insert(0, current_page - i - 1)
    
    range_extension.append(current_page)
    
    for i in range(step_right):
        range_extension.append(current_page + i + 1)

    return  {'remain_left':remain_left, 'remain_right':remain_right, 'ex_range': range_extension}
    
class StoreView(ListView):
    model = Product
    template_name = 'store/store.html'
    filter_context = {}
    
    def get_queryset(self):
        # variables initialization here 
        self.filter_context = {'query':'', 'category':'', 'minPrice':'', 'maxPrice':'', 'sortType':'', 'page':1}
        queryset = super(StoreView, self).get_queryset()

        q = self.request.GET.get("q")
        minPrice = self.request.GET.get("minPrice")
        maxPrice = self.request.GET.get("maxPrice")
        sortType = self.request.GET.get("SortType")
        page = self.request.GET.get("page");
        
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
        
        if sortType == 'price_asc':
            queryset = queryset.order_by('price')

        elif sortType == 'price_dsc':
            queryset = queryset.order_by('-price')
            
        elif sortType == 'rate':
            pass
        
        self.filter_context['sortType'] = sortType
        self.filter_context['page'] = (page,1)[page == None]
        
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
        
        # pagination at last
        pagination = Paginator(context['list_product'], 1)
        
        try:
            context['pagination'] = pagination.page(context['page'])
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            context['pagination'] = pagination.page(1)
            context['page'] = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            context['pagination'] = pagination.page(pagination.num_pages)
            context['page'] = pagination.num_pages
        
        context['pagination_ext'] = extend_pagination(context['pagination'], 2)
          
        return context
        
class ItemStoreView(DetailView):
    model = Product
    #template_name = 'store/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        
        product_medias = ProductMedia.objects.filter(product_id = context['product'].id)
        prim_media = product_medias.get(isPrimary = True)
        second_media = product_medias.filter(isPrimary = False)
        context['media'] = {}
        context['media']['primary'] = prim_media
        context['media']['secondary'] = second_media
        
        return context
    

class AjaxStoreView(View):
    pass