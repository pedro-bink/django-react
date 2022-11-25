from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register(r'employee', views.EmployeeViewSet, basename="employee")
router.register(r'department', views.DepartmentViewSet, basename="department")

urlpatterns = [
   path('', include(router.urls))
]
