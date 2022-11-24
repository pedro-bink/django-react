from django.urls import path
from . import views

urlpatterns = [
   path("department/", views.DepartmentView.as_view()),
   path("department/<int:id>/", views.DepartmentView.as_view())
]
