from django.urls import path
from . import views

urlpatterns = [
    path('', views.info),
    path('resume', views.view_resume),
    path('projects', views.view_projects),
    path('education', views.view_education)
]
