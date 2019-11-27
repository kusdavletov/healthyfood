from django.contrib import admin
from django.urls import path, include

from healthy_food import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),
    path("programs/", include("programs.urls")),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("about-us/", views.about_us, name="about_us"),
    path("contacts/", views.contacts, name="contacts"),
]
