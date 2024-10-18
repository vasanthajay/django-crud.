from django.shortcuts import render,redirect
from crudApp.models import Student
from crudApp.forms import StudentForm
# Create your views here.

def retrieve_view(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

def creat_view(request):
    form=StudentForm()
    if request.method=="POST":
     form =StudentForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/check')
    return render(request,'creat.html',{'form':form})

def delete_views(request,id):
   students=Student.objects.get(id=id)
   students.delete()
   return redirect('/check')


def update_views(request,id):
    student=Student.objects.get (id=id)
    form =StudentForm(instance=student)
    if request.method == 'POST':
        form =StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'update.html', {'form':form})


   
   
   

