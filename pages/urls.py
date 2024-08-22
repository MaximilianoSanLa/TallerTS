from django.urls import path
from .views import HomePageView,AboutPageView,contact,ProductShowView,ProductCreateView,ProductIndexView
urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contact.as_view(),name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'),
     path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]