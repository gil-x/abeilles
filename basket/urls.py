from basket.forms import TestForm
from django.urls import path
from . import views
# from basket.views import Thanks

urlpatterns = [
    path('', views.index, name='basket'),
    path('modifier', views.edit, name='edit'),
    # path('subscription', views.subscription, name='subscription'),
    path('abonnement-newsletter-panier', views.Thanks.as_view(), name='thanks'),
    path('subscription-endpoint', views.subcription_endpoint, name='subcription_endpoint')
]
