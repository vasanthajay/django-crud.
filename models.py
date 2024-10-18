from django.db import models


# Create your models here.
class Student(models.Model):
    Sno=models.IntegerField()
    Sname=models.CharField(max_length=50)
    Sclass=models.CharField(max_length=50)
    Srollno=models.IntegerField()
    Sgroup=models.CharField(max_length=50)
    Sage=models.IntegerField()
    Saddress=models.CharField(max_length=50)



# class Employee(models.Model):
#     Eno=models.IntegerField()
#     Ename=models.CharField(max_length=50)
#     Edepartment=models.CharField(max_length=50)
#     Eid=models.IntegerField()
#     Esalary=models.IntegerField()
#     Eage=models.IntegerField()
#     Eaddress=models.CharField(max_length=50)


