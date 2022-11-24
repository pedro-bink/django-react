
from django.contrib import admin
from django.urls import path, include

import employee.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(employee.urls)),
]
