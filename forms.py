from django import forms
from crudApp.models import Student

# # Create your models here.
class StudentForm(forms.ModelForm):
     class Meta:
          model=Student
          fields='__all__'
# # class Employee(models.Model):
# #     Eno=models.IntegerField()
# #     Ename=models.CharField(max_length=50)
# #     Edepartment=models.CharField(max_length=50)
# #     Eid=models.IntegerField()
# #     Esalary=models.IntegerField()
# #     Eage=models.IntegerField()
# #     Eaddress=models.CharField(max_length=50)


