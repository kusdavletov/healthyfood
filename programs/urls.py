from django.urls import path
from . import views


urlpatterns = [
    path("", views.programs, name="programs"),
    path("<int:pk>/", views.program_info, name="program_info"),
]
