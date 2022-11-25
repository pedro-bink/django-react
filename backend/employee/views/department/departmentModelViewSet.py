from rest_framework.viewsets import ModelViewSet
from employee.models import Departments
from employee.serializers import DepartmentSerializer
    
#endpoints referentes aos Departamentos feitos baseado na abordagem ModelViewSet
class DepartmentViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer