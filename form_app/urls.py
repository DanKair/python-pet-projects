from django.urls import path
from . import views

urlpatterns = [
    path('form', views.home_page, name="home"),
    path('contact/', views.contact_page, name="contact"),
    path('contact/success', views.contact_success_page, name="contact-success"),
]