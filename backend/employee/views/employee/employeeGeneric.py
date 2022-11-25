from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from employee.models import Employees
from serializers import EmployeeSerializer

#endpoints referentes aos Empregados feitos baseado na abordagem ListCreateAPIView e utilizando mixins
class EmployeesListGeneric(ListCreateAPIView):
    #queryset e serializer_class são atributos obrigatorios para o funcionamento correto da classe.
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    
class EmployeeDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
