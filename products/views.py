# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from carts.models import Cart

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    queryset = Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    queryset = Product.objects.all().featured()


class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all()


class ProductDetailSlugView(DetailView):
    template_name = "products/detail.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request) #cart part
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance