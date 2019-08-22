from django.urls import path
from .views import index, applicants_by_college


urlpatterns = [
    path("", index, name="index"),
    path("/<str:college_name>", applicants_by_college)
]
