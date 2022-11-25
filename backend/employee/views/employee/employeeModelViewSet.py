from rest_framework.viewsets import ModelViewSet
from employee.models import Employees
from employee.serializers import EmployeeSerializer
    
#endpoints referentes aos Empregados feitos baseado na abordagem ModelViewSet
class EmployeeViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer