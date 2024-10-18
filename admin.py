from django.contrib import admin
from crudApp.models import Student
# from crudApp.models import Employee
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_diplay=['Sno','Sname','Sclass','Srollno','Sgroup','Sage','Saddress']
admin.site.register(Student,StudentAdmin)





# class StudentAdmin(admin.ModelAdmin):
#     list=['Eno','Ename','Edepartment','Eid','Esalary','Eage','Eaddress'] 
# admin.site.register(Employee,StudentAdmin)



