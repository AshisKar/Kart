from django.urls import path

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('(?P<slug>[\w-]+)/', ProductDetailSlugView.as_view()),
]
