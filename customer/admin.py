from django.contrib import admin

from customer.models import Customer
from hr.models import Engineer , Department , Employee , JopType , EmployeeCategory
admin.site.register([Engineer,Department , Customer
                        , Employee , EmployeeCategory , JopType])
# Register your models here.
