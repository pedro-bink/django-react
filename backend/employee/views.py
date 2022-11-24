from django.shortcuts import HttpResponse
from django.views import View
from . models import Employees, Departments
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

from . serializer import DepartmentSerializer, EmployeeSerializer
from django.http.response import JsonResponse

@method_decorator(csrf_exempt, name="dispatch")
class DepartmentView(View):
    
    def get(self, request, id=None):
        if id:
            department = Departments.objects.get(id=id)
            departments_serialized = DepartmentSerializer(department)
            return JsonResponse(departments_serialized.data)
        else:
            departments = Departments.objects.all()
            departments_serialized = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serialized.data, safe=False)
    
    def post(self, request):
        department = JSONParser().parse(request)
        department_serialized = DepartmentSerializer(data=department)
        
        if department_serialized.is_valid():
            department_serialized.save() 
            return JsonResponse(department_serialized.data, safe=False)
        else:
            return JsonResponse("Erro ao inserir registro no banco de dados", safe=False)
        
    def put(self, request, id):
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=id)
        department_serialized = DepartmentSerializer(instance=department, data=department_data)
        
        if department_serialized.is_valid():
            department_serialized.save()
            return JsonResponse(department_serialized.data, safe=False)
        else:
            return JsonResponse("Erro ao atualizar registro", safe=False)
        
    def patch(self, request, id):
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=id)
        department_serialized = DepartmentSerializer(instance=department, data=department_data)
        
        if department_serialized.is_valid():
            department_serialized.save()
            return JsonResponse(department_serialized.data, safe=False)
        else:
            return JsonResponse("Erro ao atualizar registro", safe=False)
        
    def delete(self, request, id):
        department = Departments.objects.get(id=id)
        department.delete()
        return JsonResponse("Registro deletado do banco de dados", safe=False)