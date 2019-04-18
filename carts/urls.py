from django.conf.urls import re_path

from .views import (
        cart_home,
        cart_update,
        )

urlpatterns = [
    re_path(r'^$', cart_home, name='home'),
    re_path(r'^update/$', cart_update, name='update'),
]