
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')

import django
django.setup()


from crudApp.models import *
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fSno=randint(1,1001)
        fSname=faker.name()
        fSclass=randint(1,10)
        fSrollno=randint(1,10)
        fSgroup=faker.name()
        fSage=randint(20,30)
        fSaddress=faker.city()
        Stud_record=Student.objects.get_or_create(Sno=fSno,Sname=fSname,Sclass=fSclass,Srollno=fSrollno,Sgroup=fSgroup,Sage=fSage,Saddress=fSaddress)

        generate(20)

