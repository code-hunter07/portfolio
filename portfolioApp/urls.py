from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("blogdetails", views.blogdetails, name="blogdetails"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("services", views.services, name="services")

]