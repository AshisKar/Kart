from django.conf.urls import re_path

from .views import (
    SearchProductView
)

urlpatterns = [
    re_path(r'^$', SearchProductView.as_view(), name='list'),
]
