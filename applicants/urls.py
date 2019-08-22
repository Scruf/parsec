from django.urls import path
from .views import index, applications_by_name

urlpatterns = [
    path('', index, name='index'),
    path('/<str:applicant_name>', applications_by_name)
]
