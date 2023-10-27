from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.index, name='services'),
    path('service/<str:service_slug>/', views.service, name="single-service"),
    

    # new URLs
    # path('professionnels/', views.services_professionnels, name="services_pro2"),

    # path('professionnels/', views.services_pro, name="services_pro2"),
    # path('particuliers/', views.services_ind, name="services_ind2"),
    # path('professionnels/', TemplateView.as_view(template_name='services/test.html'), name="servicespro"),

    # path('<str:job>/demande', views.single, name="ask-service"),

    path('<str:category_slug>/', views.category, name="category"),
]