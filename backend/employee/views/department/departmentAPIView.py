from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from serializers import DepartmentSerializer
from employee.models import Departments

#endpoints referentes ao Departamento feitos baseado na abordagem APIView e utilizando os Serializers
@method_decorator(csrf_exempt, name="dispatch")
class DepartmentView(APIView):
    def get(self, request, id=None):
        if id:
            department = get_object_or_404(Departments, id=id)
            departments_serialized = DepartmentSerializer(department)
            return Response(departments_serialized.data, status=status.HTTP_200_OK)
        else:
            departments = Departments.objects.all()
            departments_serialized = DepartmentSerializer(departments, many=True)
            print(departments_serialized.data)
            return Response(departments_serialized.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        department_serialized = DepartmentSerializer(data=request.data)
        if department_serialized.is_valid():
            department_serialized.save() 
            return Response(department_serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(department_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        department = get_object_or_404(Departments, id=id)
        department_serialized = DepartmentSerializer(instance=department, data=request.data)
        if department_serialized.is_valid():
            department_serialized.save()
            return Response(department_serialized.data, status=status.HTTP_200_OK)
        else:
            return Response("department_serialized.errors", status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        department = Departments.objects.get(id=id)
        department_serialized = DepartmentSerializer(instance=department, data=department.data)
        
        if department_serialized.is_valid():
            department_serialized.save()
            return Response(department_serialized.data)
        else:
            return Response("Erro ao atualizar registro")
        
    def delete(self, request, id):
        department = get_object_or_404(Departments, id=id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)